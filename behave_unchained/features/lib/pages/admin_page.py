from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from behave_unchained.features import environment
from behave_unchained import passwords


class AdminPage(BasePage):
    locator_dictionary = {
        'username_field': (By.ID, 'id_username'),
        'password_field': (By.ID, 'id_password'),
        'submit_button': (By.CSS_SELECTOR, '#login-form > div.submit-row > input[type="submit"]'),
        'dashboard': (By.CLASS_NAME, ' dashboard')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=environment.ADMIN_URL)

    def log_in(self, username=environment.ADMIN_USERNAME, password=passwords.ADMIN_PASSWORD):
        self.find_element(*self.locator_dictionary['username_field']).send_keys(username)
        self.find_element(*self.locator_dictionary['password_field']).send_keys(password)
        self.find_element(*self.locator_dictionary['submit_button']).click()

    def is_logged_in(self):
        if self.find_element(*self.locator_dictionary['dashboard']):
            return True
        else:
            return False
