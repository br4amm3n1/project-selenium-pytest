from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL is not corrected."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
               "Login form isn't exist"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), \
               "Register form isn't exist"

    def register_new_user(self, email: str, password: str) -> None:
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

        password_field_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FIELD)
        password_field_confirm.send_keys(password)

        submit_button = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT_REG)
        submit_button.click()
