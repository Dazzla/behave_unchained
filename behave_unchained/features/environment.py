import logging
import time
import os
import shutil
from selenium import webdriver

BASE_URL = "http://127.0.0.1:8000/"
ADMIN_URL = BASE_URL + 'admin/'
ADMIN_USERNAME = 'admin'


def before_feature(context, feature):
    print("Before feature\n")
    # Create logger
    # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
    context.logger = logging.getLogger('seleniumframework_tests')
    handler = logging.FileHandler('./seleniumframework_tests.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    context.logger.addHandler(handler)
    context.logger.setLevel(logging.DEBUG)

    print("User data:", context.config.userdata)
    # behave -D BROWSER=chrome
    initialise_browser(context)
    print("Before scenario\n")


def initialise_browser(context):
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'
    if BROWSER == 'chrome':
        context.browser = webdriver.Chrome()
    elif BROWSER == 'firefox':
        context.browser = webdriver.Firefox()
    elif BROWSER == 'safari':
        context.browser = webdriver.Safari()
    elif BROWSER == 'ie':
        context.browser = webdriver.Ie()
    elif BROWSER == 'opera':
        context.browser = webdriver.Opera()
    elif BROWSER == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        print("Browser you entered:", BROWSER, "is invalid value")
    context.browser.maximize_window()


def after_scenario(context, scenario):
    print("scenario status")
    print(scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")


def after_feature(context, feature):
    print("\nAfter Feature")
    context.browser.quit()


def after_all(context):
    print("User data:", context.config.userdata)
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("failed_scenarios_screenshots"):
            os.rmdir("failed_scenarios_screenshots")
            os.makedirs("failed_scenarios_screenshots")
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
                time.strftime("%d_%m_%Y"),
                'zip',
                "failed_scenarios_screenshots")
            # os.rmdir("failed_scenarios_screenshots")
            print("Executing after all")
