from behave import *
from behave_unchained.features import environment
from behave_unchained.features.lib.pages.polls_page import PollsPage


use_step_matcher("re")


@step("I am on the (?P<page_type>\w+) page")
def step_impl(context, page_type):
    polls_page = PollsPage(context)
    polls_page.visit(environment.BASE_URL + page_type + '/')
    polls_page.is_displayed()
    assert(polls_page.is_displayed())


@step("I(?: am on| can access) a question page")
def step_impl(context):
    polls_page = PollsPage(context)
    polls_page.first_question_link().click()
