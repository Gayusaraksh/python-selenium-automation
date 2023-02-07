import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service=Service('/Users/bala/Automation/python-selenium-automation/chromedriver')
driver=webdriver.Chrome(service=service)

driver.get('https://www.amazon.com')

driver.find_element(By.XPATH,"//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
time.sleep(1)

expected_result='Sign in'
actual_result=driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']").text
print(actual_result)
assert actual_result == expected_result,f'expected_result is {expected_result} but actual result is {actual_result}'
print("Test case Passed")

expected_result1='Email or mobile phone number'
actual_result1=driver.find_element(By.XPATH,"//label[@for='ap_email']").text
print(actual_result1)
assert actual_result1 == expected_result1,f'expected_result is {expected_result1} but actual_result is {actual_result1}'
print("Test case Passed")

driver.find_element(By.ID,"ap_email").is_displayed()
print("Email field is displayed")