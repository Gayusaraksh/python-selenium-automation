import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


VERIFY_LINKS = (By.CSS_SELECTOR,'div[class*="zg-nav-tab-all_style_zg-tabs-li"]')
CURRENT_LINK = (By.CSS_SELECTOR,'a[href*="/ref=zg_bs_tab"]')
BANNER_TEXT = (By.ID, "zg_banner_text")

@then('Verify {expected_amount} links are present on the Best Sellers page')
def verify_link(context,expected_amount):
    expected_amount = int(expected_amount)
    actual_result = context.driver.wait.until(EC.visibility_of_all_elements_located(VERIFY_LINKS))
    actual_result = context.driver.find_elements(*VERIFY_LINKS)
    assert len(actual_result) == expected_amount, f'Actual result not same as expected amount'


@then('Click on each top links and check correct page opened')
def click_each_top_links(context):
    #context.actual_result = context.driver.wait.until(EC.visibility_of_all_elements_located(VERIFY_LINKS))
    expected_banner_text = ["Amazon Best Sellers", "Amazon Hot New Releases", "Amazon Movers & Shakers", "Amazon Most Wished For", "Amazon Gift Ideas"]
    all_links = len(context.driver.find_elements(*VERIFY_LINKS))
    for i in range(0, all_links):
        links = context.driver.find_elements(*VERIFY_LINKS)
        links[i].click()
        banner = context.driver.find_element(*BANNER_TEXT).text
        assert banner in expected_banner_text, f"Unexpected Banner Text found: {banner}"
        time.sleep(1)




    # for i in range(len(context.actual_result)):
    #     context.actual_result1 = context.driver.find_elements(*VERIFY_LINKS)
    #     context.actual_result1[i].click()
    #     # current_link = context.driver.wait.until(EC.visibility_of_all_elements_located(CURRENT_LINK))
    #     print(context.actual_result1[i])

