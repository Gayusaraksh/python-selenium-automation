from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com")
    #context.driver.refresh()


@when('Click on Orders button')
def click_orders(context):
    context.driver.find_element(By.XPATH,"//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()


@then('Verify that the {expected_result} header is visible in sign in page')
def signin_header(context,expected_result ):
    actual_result = context.driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']").text
    assert actual_result==expected_result, f'expected result is {expected_result} but actual result is {actual_result}'


@then('Verify that {expected_result1} label is present in sign in page')
def email_label(context,expected_result1):
    actual_result1=context.driver.find_element(By.XPATH,"//label[@for='ap_email']").text
    assert actual_result1 == expected_result1,f'expected_result is {expected_result1} but actual_result is {actual_result1}'


@then('Verify that the Email input field is present in sign in page')
def email_textbox(context):
    context.driver.find_element(By.ID,"ap_email").is_displayed()
    print("Email field is displayed")