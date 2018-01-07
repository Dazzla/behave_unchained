from .base_page_object import BasePage
from behave_unchained.features import environment
from selenium.webdriver.common.by import By


class VotePage(BasePage):
    pass

    locator_dictionary = {
        "page_text": (By.TAG_NAME, 'body'),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=environment.BASE_URL)

    def is_displayed(self):
        return self.find_element(*self.locator_dictionary['page_text']).text.__contains__("You're voting on")
