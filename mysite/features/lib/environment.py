from selenium import webdriver
BASE_URL = "http://127.0.0.1:8000/"
ADMIN_URL = BASE_URL + 'admin/'
ADMIN_USERNAME = 'dazzla'


def before_feature(context, feature):
    print("Before feature\n")
    # Create logger
    # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
    context.logger = logging.getLogger('seleniumframework_tests')
    hdlr = logging.FileHandler('./seleniumframework_tests.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    context.logger.addHandler(hdlr)
    context.logger.setLevel(logging.DEBUG)