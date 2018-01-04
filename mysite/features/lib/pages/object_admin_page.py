from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from mysite.features import environment

class ObjectAdminPage(BasePage):
    locator_dictionary = {
        'add_object_link': (By.CLASS_NAME, 'addlink')
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
