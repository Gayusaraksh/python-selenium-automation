from selenium.webdriver.common.by import By
from behave import given, when, then


WELCOME_TEXT = (By.XPATH,'//h1[text()="Welcome to Amazon Customer Service"]')
CARD_CONTAINER = (By.CSS_SELECTOR,'div.issue-card-container')
SEARCH_HELP_LIBRARY = (By.XPATH,'//h2[text()="Search our help library"]')
QUESTIONS_INPUT_FIELD = (By.CSS_SELECTOR,'input#hubHelpSearchInput')
ALL_HELP_TOPICS = (By.XPATH,'//h2[text()="All help topics"]')
RECOMMENDED_TOPICS = (By.CSS_SELECTOR,'ul.help-topics')


@then('Check {expected_text} text is present on the page')
def welcome_text(context,expected_text):
    actual_text = context.driver.find_element(*WELCOME_TEXT).text
    assert actual_text == expected_text,f'{expected_text} is not same as {actual_text}'


@then('Check Table of contents present on the page')
def card_container(context):
    actual_result = context.driver.find_element(*CARD_CONTAINER).is_displayed()
    print(actual_result)


@then('Check {expected_text} is present on the page')
def search_help_library(context,expected_text):
    actual_text = context.driver.find_element(*SEARCH_HELP_LIBRARY).text
    assert actual_text == expected_text, f'{expected_text} is not same as {actual_text}'


@then('Check {search_field} shown in the page')
def search_field(context,search_field):
    actual_text = context.driver.find_element(*QUESTIONS_INPUT_FIELD)
    print(actual_text)


@then('Check {expected_text} present on the page')
def all_help_topics(context,expected_text):
    actual_text = context.driver.find_element(*ALL_HELP_TOPICS).text
    assert actual_text == expected_text,f'{expected_text} is not same as {actual_text}'


@then('Check Recommended Topics present on the customer service page')
def recommended_topics(context):
    actual_text = context.driver.find_element(*RECOMMENDED_TOPICS).is_displayed()
    print(actual_text)

