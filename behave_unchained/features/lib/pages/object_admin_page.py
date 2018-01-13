from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from behave_unchained.features import environment


class AdminDashboard(BasePage):
    locator_dictionary = {
        'add_object_link': (By.CLASS_NAME, 'addlink'),
        'question_admin_link': (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr/th/a'),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=environment.ADMIN_URL)

    def is_displayed(self):
        if self.find_element(*self.locator_dictionary['add_object_link']):
            return True
        else:
            return False

    def access_question_admin_page(self):
        self.find_element(*self.locator_dictionary['question_admin_link']).click()
