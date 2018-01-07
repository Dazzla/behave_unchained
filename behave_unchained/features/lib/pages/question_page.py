from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from behave_unchained.features import environment


class QuestionPage(BasePage):

    locator_dictionary = {
        "page_text": (By.TAG_NAME, 'body')
    }


    def is_displayed(self):
