from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Add to cart')
def add_cart(context):
    context.app.product_page.add_to_cart()


@then('Verify user can click through colors')
def click_colors(context):
    context.app.product_page.click_colors()