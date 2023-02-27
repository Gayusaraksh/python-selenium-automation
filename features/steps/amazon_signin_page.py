from selenium.webdriver.common.by import By
from behave import given, when, then


SIGN_IN_HEADER = (By.XPATH,"//h1[@class='a-spacing-small']")
EMAIL_LABEL = (By.XPATH,"//label[@for='ap_email']")
EMAIL_TEXTBOX = (By.ID,"ap_email")


@then('Verify that the {expected_result} header is visible in sign in page')
def signin_header(context,expected_result ):
    actual_result = context.driver.find_element(*SIGN_IN_HEADER).text
    assert actual_result==expected_result, f'expected result is {expected_result} but actual result is {actual_result}'


@then('Verify that {expected_result1} label is present in sign in page')
def email_label(context,expected_result1):
    actual_result1=context.driver.find_element(*EMAIL_LABEL).text
    assert actual_result1 == expected_result1,f'expected_result is {expected_result1} but actual_result is {actual_result1}'


@then('Verify that the Email input field is present in sign in page')
def email_textbox(context):
    context.driver.find_element.is_displayed()
    print("Email field is displayed")