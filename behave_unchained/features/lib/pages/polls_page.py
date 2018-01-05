from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from behave_unchained.features import environment


class PollsPage(BasePage):
    locator_dictionary = {
        "page_header": (By.TAG_NAME, 'h1'),
        "page_text": (By.TAG_NAME, 'body')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=environment.BASE_URL)

    def is_displayed(self):
        header_text = self.find_element(*self.locator_dictionary['page_header']).text
        if 'Polls Page' in header_text:
            return True
        else:
            return False
