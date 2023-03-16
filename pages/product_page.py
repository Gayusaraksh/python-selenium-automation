import time
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(Page):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'input#add-to-cart-button')
    CLICK_COLORS = (By.CSS_SELECTOR, 'div#variation_color_name li')
    CURRENT_COLOR = (By.CSS_SELECTOR, 'span.selection')
    CURRENT_PRICE = (By.CSS_SELECTOR, 'span.a-price-whole')

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def click_colors(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.CLICK_COLORS))
        all_colors = self.driver.find_elements(*self.CLICK_COLORS)
        for color in all_colors:
            color.click()
            time.sleep(2)
            current_color = self.driver.wait.until(EC.visibility_of_element_located(self.CURRENT_COLOR)).text

            print('Current color is: ', current_color)
            current_price = self.driver.find_element(*self.CURRENT_PRICE).text
            print('Current price is ', current_price)
