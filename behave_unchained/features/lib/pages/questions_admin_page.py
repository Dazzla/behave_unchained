from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from behave_unchained.features import environment


class QuestionsAdminPage(BasePage):

    locator_dictionary = {
        'results_table': (By.ID, 'result_list')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=environment.BASE_URL)

    def is_displayed(self):
        return self.find_element(*self.locator_dictionary['results_table']).is_displayed()
