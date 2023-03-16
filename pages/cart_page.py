from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    CART_EMPTY = (By.CSS_SELECTOR,'div[class="a-row sc-your-amazon-cart-is-empty"]')

    def verify_cart_empty(self , expected_text ):
        self.verify_text(expected_text,*self.CART_EMPTY)
