from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def open_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, email, password):
        self.open_login_page()
        self.type(LoginLocators.EMAIL, email)
        self.type(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)
