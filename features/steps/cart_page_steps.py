from behave import given, when, then


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()


@then('Verify that {expected_result} is shown in the cart page')
def cart_empty(context,expected_result):
    context.app.cart_page.verify_cart_empty(expected_result)

