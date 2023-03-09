from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_NOTICE = (By.CSS_SELECTOR,'a[href="https://www.amazon.com/privacy"]')


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.windows = context.driver.window_handles
    print(context.windows)
    context.driver.switch_to.window(context.windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?'))


@then('User can close new window')
def close_new_window(context):
    context.driver.close()


@then('User switch back to original window')
def switch_back_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
