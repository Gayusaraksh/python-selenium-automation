from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BUTTON = (By.CSS_SELECTOR,'img[alt="Montana West Hobo Purses and Handbags for Women Vegan Leather Top Handle Shoulder Handbags with Zipper"]')

@when('Select item from the search list')
def select_item(context):
    context.driver.find_element(*SEARCH_BUTTON).click()



