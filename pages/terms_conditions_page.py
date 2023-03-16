from pages.base_page import Page
from selenium.webdriver.common.by import By


class TermsConditionsPage(Page):
    PRIVACY_NOTICE = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')

    def open_tc_page(self):
        self.open_url('gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088%27)')

    def store_original_windows(self):
        self.store_window()

    def click_privacy_notice_link(self):
        self.click(*self.PRIVACY_NOTICE)

