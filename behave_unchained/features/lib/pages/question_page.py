from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from behave_unchained.features import environment


class QuestionPage(BasePage):
    def __init__(self, context, question_id=''):
        BasePage.__init__(
            self,
            context.browser,
            base_url=environment.BASE_URL + question_id + '/')
