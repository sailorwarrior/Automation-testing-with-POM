from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "current URL does not contain 'login'"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "registration form is not presented"
        assert True
