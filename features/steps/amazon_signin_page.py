from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify that the {expected_result} header is visible in sign in page')
def signin_header(context,expected_result ):
    context.app.sign_in_page.verify_header(expected_result)


@then('Verify that {expected_result1} label is present in sign in page')
def email_label(context,expected_result1):
    context.app.sign_in_page.verify_label(expected_result1)


@then('Verify that the Email input field is present in sign in page')
def email_textbox(context):
    context.app.sign_in_page.verify_email_field()
