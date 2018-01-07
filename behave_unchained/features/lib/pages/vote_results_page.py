from .base_page_object import BasePage
from behave_unchained.features import environment
from selenium.webdriver.common.by import By


class VoteResultsPage(BasePage):

    locator_dictionary = {
        "vote_again_link": (By.ID, 'vote_again_link')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=environment.BASE_URL)

    def is_displayed(self):
        return self.find_element(*self.locator_dictionary['vote_again_link'])
