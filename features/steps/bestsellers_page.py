import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


BEST_SELLERS_LINK = (By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
VERIFY_LINKS = (By.CSS_SELECTOR,'div[class*="_p13n-zg-nav-tab-all_style_zg-tabs-li"]')


@when('Click on Best Sellers link')
def best_sellers_link(context):
    context.driver.wait.until(EC.element_to_be_clickable(BEST_SELLERS_LINK)).click()


@then('Verify {expected_amount} links are present on the Best Sellers page')
def verify_link(context,expected_amount):
    expected_amount=int(expected_amount)
    context.driver.wait.until(EC.visibility_of_all_elements_located(VERIFY_LINKS))
    actual_result = context.driver.find_elements(*VERIFY_LINKS)
    assert len(actual_result) == expected_amount, f'Actual result not same as expected amount'

