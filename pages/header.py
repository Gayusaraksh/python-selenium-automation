import time
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    AMAZON_SEARCH_BOX = (By.CSS_SELECTOR, 'input#twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, 'input#nav-search-submit-button')
    ORDERS_ICON = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    CART_ICON = (By.CSS_SELECTOR, 'a[href="/gp/cart/view.html?ref_=nav_cart"]')
    CART_ITEMS_COUNT = (By.CSS_SELECTOR, 'span#nav-cart-count')
    BEST_SELLERS_LINK = (By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
    VERIFY_LINKS = (By.CSS_SELECTOR, 'div[class*="zg-nav-tab-all_style_zg-tabs-li"]')
    CURRENT_LINK = (By.CSS_SELECTOR, 'a[href*="/ref=zg_bs_tab"]')
    BANNER_TEXT = (By.ID, "zg_banner_text")
    CUSTOMER_SERVICE_LINK = (By.XPATH, '//a[text()="Customer Service"]')

    def search_input(self,text):
        self.input_text(text, *self.AMAZON_SEARCH_BOX)

    def click_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS_ICON)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def check_cart_count(self,expected_count):
        self.verify_text(expected_count,*self.CART_ITEMS_COUNT)

    def click_best_sellers(self):
        self.click(*self.BEST_SELLERS_LINK)

    def verify_top_links(self,expected_amount):
        expected_amount = int(expected_amount)
        actual_result = self.driver.wait.until(EC.visibility_of_all_elements_located(self.VERIFY_LINKS))
        actual_result = self.driver.find_elements(*self.VERIFY_LINKS)
        assert len(actual_result) == expected_amount, f'Actual result not same as expected amount'

    def verify_correct_page_opens(self):
        expected_banner_text = ["Amazon Best Sellers", "Amazon Hot New Releases", "Amazon Movers & Shakers","Amazon Most Wished For", "Amazon Gift Ideas"]
        all_links = len(self.driver.find_elements(*self.VERIFY_LINKS))
        for i in range(0, all_links):
            links = self.driver.find_elements(*self.VERIFY_LINKS)
            links[i].click()
            banner = self.driver.find_element(*self.BANNER_TEXT).text
            assert banner in expected_banner_text, f"Unexpected Banner Text found: {banner}"
            time.sleep(1)

    def click_customer_service(self):
        self.click(*self.CUSTOMER_SERVICE_LINK)

