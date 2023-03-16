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
    context.app.customer_service_page.verify_welcome_text(expected_text)


@then('Check Table of contents present on the page')
def card_container(context):
    context.app.customer_service_page.verify_card_container()


@then('Check {expected_text} is present on the page')
def search_help_library(context,expected_text):
    context.app.customer_service_page.verify_search_help_library(expected_text)


@then('Check Search box shown in the page')
def search_field(context):
    context.app.customer_service_page.verify_search_query_field()


@then('Check {expected_text} present on the page')
def all_help_topics(context,expected_text):
    context.app.customer_service_page.verify_all_help_topics(expected_text)


@then('Check Recommended Topics present on the customer service page')
def recommended_topics(context):
    context.app.customer_service_page.verify_recommended_topics()
