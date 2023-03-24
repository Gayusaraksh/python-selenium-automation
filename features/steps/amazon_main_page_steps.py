from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@given('Open amazon product page {end_url}')
def open_amazon_prod_page(context,end_url):
    context.app.main_page.open_product_page()


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


@when('Select department by alias {alias}')
def select_dept(context,alias):
    context.app.header.select_dept_by_alias(alias)


@when('Hover over language options')
def hover_over_language(context):
    context.app.header.hover_over_lang()


@then('Check for {expected_count} item in the cart')
def cart_number(context, expected_count):
    context.app.header.check_cart_count(expected_count)


@then('Verify spanish option present')
def spanish_present(context):
    context.app.header.check_spanish_present()






