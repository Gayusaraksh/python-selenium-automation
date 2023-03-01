import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SELECT_BUTTON = (By.CSS_SELECTOR,'img[alt="Montana West Hobo Purses and Handbags for Women Vegan Leather Top Handle Shoulder Handbags with Zipper"]')
ALL_PRODUCT_NAME = (By.CSS_SELECTOR,'span.a-size-base-plus.a-color-base.a-text-normal')
ALL_PRODUCT_IMAGE = (By.CSS_SELECTOR,'img.s-image')


@when('Select item from the search list')
def select_item(context):
    context.driver.find_element(*SELECT_BUTTON).click()


@then('Verify that every product on Amazon search results page has product name')
def results_all_product_name(context):
    all_product_name = context.driver.find_elements(*ALL_PRODUCT_NAME)
    print("Number of elements: ", len(all_product_name))
    for name in all_product_name:
        print(name.text)


@then('Verify that every product on Amazon search results page has product image')
def results_all_product_image(context):
    all_product_image = context.driver.find_elements(*ALL_PRODUCT_IMAGE)
    for image in all_product_image:
        print(image.is_displayed())