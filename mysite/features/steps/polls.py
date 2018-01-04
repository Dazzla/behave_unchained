from behave import *
from selenium import webdriver
from behave import use_step_matcher
from mysite.features.lib import environment, passwords

use_step_matcher("re")

browser = webdriver.Chrome()


def after_feature():
    browser.close()


@given("I am on the (?P<page>\w+) page")
def step_impl(context, page):
    browser.get(environment.BASE_URL + page)


@then("I can see the text '(?P<expected_page_text>Hello, world. You're at the polls index.)'")
def step_impl(context, expected_page_text):
    header_text = browser.find_element_by_tag_name('body').text
    assert(expected_page_text in header_text)


@given("I access '(?P<page_identifier>\S+)' admin")
def step_impl(context, page_identifier):
    browser.get(environment.ADMIN_URL + page_identifier)
    assert(browser.find_element_by_class_name('addlink'))
    pass


@given("I am logged in as an administrator")
def step_impl(context):
    browser.get(environment.ADMIN_URL)
    username_field = browser.find_element_by_id('id_username')
    password_field = browser.find_element_by_id('id_password')
    username_field.send_keys(environment.ADMIN_USERNAME)
    password_field.send_keys(passwords.ADMIN_PASSWORD)
    submit_button = browser.find_element_by_css_selector('#login-form > div.submit-row > input[type="submit"]')
    submit_button.click()
    dashboard = browser.find_element_by_class_name(' dashboard')
    assert('Question' in dashboard.text)
