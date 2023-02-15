from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Enter {searchterm} in the search box')
def items_search(context,searchterm):
    context.driver.find_element(By.CSS_SELECTOR,'input#twotabsearchtextbox').send_keys(searchterm)


@when('Select item from the search list')
def select_item(context):
    context.driver.find_element(By.CSS_SELECTOR,'img[alt="Montana West Hobo Purses and Handbags for Women Vegan Leather Top Handle Shoulder Handbags with Zipper"]').click()


@when('Click on Add to cart')
def add_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'input#add-to-cart-button').click()


@then('Check for the number of items in the cart')
def cart_number(context):
    count=context.driver.find_element(By.CSS_SELECTOR,'span#nav-cart-count').text
    print(count)




