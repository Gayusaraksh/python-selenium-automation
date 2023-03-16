from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver , 15)
        self.base_url = "https://www.amazon.com/"

    def open_url(self,end_url=''):
        self.driver.get(f'{self.base_url}{end_url}')

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self,text,*locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)
        print('Input text is', text)

    def wait_for_element_click(self,*locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_disappear(self,*locator):
        self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self,*locator):
        self.driver.wait.until(EC.visibility_of_element_located(locator))

    def verify_text(self,expected_text,*locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text ,f'expected text is {expected_text} but got {actual_text}'

    def verify_partial_text(self, expected_text,*locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text in expected_text,f'{actual_text} is not in {expected_text}'

    def verify_url_contains_query(self,query):
        self.driver.wait.until(EC.url_contains(query))

    def verify_if_displayed(self,*locator):
        self.driver.find_element(*locator).is_displayed()

    def store_window(self):
        self.driver.original_window = self.driver.current_window_handle

    def switch_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        self.windows = self.driver.window_handles
        print(self.windows)
        self.driver.switch_to.window(self.windows[1])

    def switch_back_to_original_window(self):
        self.driver.switch_to.window(self.driver.original_window)

    def close_window(self):
        self.driver.close()



