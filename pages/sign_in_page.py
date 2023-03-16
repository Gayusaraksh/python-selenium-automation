from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    SIGN_IN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_LABEL = (By.XPATH, "//label[@for='ap_email']")
    EMAIL_TEXTBOX = (By.ID, "ap_email")

    def verify_header(self,expected_text):
        self.verify_text(expected_text,*self.SIGN_IN_HEADER)

    def verify_label(self,expected_text):
        self.verify_text(expected_text,*self.EMAIL_LABEL)

    def verify_email_field(self):
        self.verify_textbox(*self.EMAIL_TEXTBOX)



