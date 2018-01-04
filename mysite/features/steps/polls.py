from selenium import webdriver
from mysite.features.lib import passwords
from mysite.features import environment
from behave import *
from mysite.features.lib.pages.polls_page import PollsPage
from mysite.features.lib.pages.admin_page import AdminPage
from mysite.features.lib.pages.object_admin_page import ObjectAdminPage

use_step_matcher("re")


@step("I can see the text '(?P<expected_page_text>Hello, world. You're at the polls index.)' on the polls page")
def step_impl(context, expected_page_text):
    polls_page = PollsPage(context)
    polls_page.visit(environment.BASE_URL + 'polls/')
    print(polls_page.is_displayed())
    assert(polls_page.is_displayed())


@given("I access object admin")
def step_impl(context):
    object_admin = ObjectAdminPage(context)
    object_admin.visit(environment.ADMIN_URL + 'polls/question')
    assert(object_admin.is_displayed())


@given("I am logged in as an administrator")
def step_impl(context):
    admin_page = AdminPage(context)
    admin_page.visit(environment.ADMIN_URL)
    admin_page.log_in(environment.ADMIN_USERNAME, passwords.ADMIN_PASSWORD)
    assert(admin_page.is_logged_in())
