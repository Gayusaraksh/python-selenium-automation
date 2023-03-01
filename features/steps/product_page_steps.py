import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,'input#add-to-cart-button')
CLICK_COLORS = (By.CSS_SELECTOR,'div#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR,'span.selection')
CURRENT_PRICE = (By.CSS_SELECTOR,'span.a-price-whole')

@when('Click on Add to cart')
def add_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@then('Verify user can click through colors')
def click_colors(context):
    context.driver.wait.until(EC.element_to_be_clickable(CLICK_COLORS))
    all_colors = context.driver.find_elements(*CLICK_COLORS)
    for color in all_colors:
        color.click()
        current_color = context.driver.wait.until(EC.visibility_of_element_located(CURRENT_COLOR)).text
        print('Current color is: ', current_color)
        current_price = context.driver.find_element(*CURRENT_PRICE).text
        print('Current price is ', current_price)
