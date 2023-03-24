from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Add to cart')
def add_cart(context):
    context.app.product_page.add_to_cart()


@when('Hover over new arrivals')
def hover_over_new_arrivals(context):
    context.app.header.hover_over_new_arr()


@then('Verify user can click through colors')
def click_colors(context):
    context.app.product_page.click_colors()


@then('Verify user sees the deals')
def verify_women_deals(context):
    context.app.header.check_women_present()