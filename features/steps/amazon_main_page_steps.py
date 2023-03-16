from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Enter {text} in the search box')
def items_search(context,text):
    context.app.header.search_input(text)


@when('Click on search icon')
def click_search_icon(context):
    context.app.header.click_search_icon()


@when('Click on Customer Service link')
def customer_service_link(context):
    context.app.header.click_customer_service()


@when('Click on Orders button')
def click_orders(context):
    context.app.header.click_orders()


@when('Click on Best Sellers link')
def best_sellers_link(context):
    context.app.header.click_best_sellers()


@then('Check for {expected_count} item in the cart')
def cart_number(context, expected_count):
    context.app.header.check_cart_count(expected_count)







