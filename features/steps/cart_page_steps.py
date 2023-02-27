from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ICON = (By.CSS_SELECTOR,'a[href="/gp/cart/view.html?ref_=nav_cart"]')


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify that {expected_result} is shown in the cart page')
def cart_empty(context,expected_result):
    actual_result=context.driver.find_element(By.CSS_SELECTOR,'div[class="a-row sc-your-amazon-cart-is-empty"]').text
    assert actual_result == expected_result,f'Expected result is {expected_result} but actual result is {actual_result}'


