from pages.base_page import Page


class PrivacyNoticePage(Page):

    def switch_to_new_windows(self):
        self.switch_window()

    def verify_privacy_notice_page_opened(self):
        self.verify_url_contains_query('https://www.amazon.com/gp/help/customer/display.html?')

    def close_new_window(self):
        self.close_window()

    def switch_back_to_original_windows(self):
        self.switch_back_to_original_window()