from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from mysite.features import environment


class PollsPage(BasePage):
    locator_dictionary = {
        "page_text": (By.TAG_NAME, 'body')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=environment.BASE_URL)

    def is_displayed(self):
        if self.find_element(*self.locator_dictionary['page_text']):
            return True
        else:
            return False
