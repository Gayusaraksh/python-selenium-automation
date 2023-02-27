from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,'input#add-to-cart-button')


@when('Click on Add to cart')
def add_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
