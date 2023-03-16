from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.app.terms_conditions_page.open_tc_page()


@when('Store original windows')
def store_original_window(context):
    context.app.terms_conditions_page.store_original_windows()


@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_notice_link(context):
    context.app.terms_conditions_page.click_privacy_notice_link()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.privacy_notice_page.switch_to_new_windows()


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.app.privacy_notice_page.verify_privacy_notice_page_opened()


@then('User can close new window')
def close_new_window(context):
    context.app.privacy_notice_page.close_window()


@then('User switch back to original window')
def switch_back_to_original_window(context):
    context.app.privacy_notice_page.switch_back_to_original_windows()