from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


AMAZON_SEARCH_BOX = (By.CSS_SELECTOR,'input#twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, 'input#nav-search-submit-button')
CART_ITEMS_COUNT = (By.CSS_SELECTOR,'span#nav-cart-count')
ORDERS_ICON = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
CUSTOMER_SERVICE_LINK = (By.CSS_SELECTOR,'a[data-csa-c-content-id="nav_cs_customerservice"]')
BEST_SELLERS_LINK = (By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com")
    context.driver.refresh()


@when('Enter {searchterm} in the search box')
def items_search(context,searchterm):
    context.driver.find_element(*AMAZON_SEARCH_BOX).send_keys(searchterm)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on Customer Service link')
def customer_service_link(context):
    context.driver.find_element(*CUSTOMER_SERVICE_LINK).click()


@when('Click on Orders button')
def click_orders(context):
    context.driver.find_element(*ORDERS_ICON).click()

@when('Click on Best Sellers link')
def best_sellers_link(context):
    context.driver.wait.until(EC.element_to_be_clickable(BEST_SELLERS_LINK)).click()


@then('Check for {expected_count} item in the cart')
def cart_number(context, expected_count):
    count = context.driver.find_element(*CART_ITEMS_COUNT).text
    assert count == expected_count, f'Both are not same'







