from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from behave_unchained.features import environment


class QuestionPage(BasePage):

    locator_dictionary = {
        "page_text": (By.TAG_NAME, 'body'),
        "first_choice": (By.ID, 'choice1'),
        "submit_button": (By.ID, 'submit_button')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=environment.BASE_URL)

    def is_displayed(self):
        return self.find_element(*self.locator_dictionary['first_choice'])

    def vote_in_poll(self):
        assert self.is_displayed()
        self.find_element(*self.locator_dictionary['first_choice']).click()
        self.find_element(*self.locator_dictionary['submit_button']).click()
