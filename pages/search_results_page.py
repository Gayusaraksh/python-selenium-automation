from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SELECT_BUTTON = (By.CSS_SELECTOR,'img[alt="Montana West Hobo Purses and Handbags for Women Vegan Leather Top Handle Shoulder Handbags with Zipper"]')
    ALL_PRODUCT_NAME = (By.CSS_SELECTOR, 'span.a-size-base-plus.a-color-base.a-text-normal')
    ALL_PRODUCT_IMAGE = (By.CSS_SELECTOR, 'img.s-image')
    SUBNAV = (By.CSS_SELECTOR, 'div#nav-subnav[data-category="{category}"]')


    def get_subnav_locator(self, category):
        return [self.SUBNAV[0],self.SUBNAV[1].replace("{category}",category)]

    def select_product(self):
        self.click(*self.SELECT_BUTTON)

    def results_all_product_name(self):
        all_product_name = self.driver.find_elements(*self.ALL_PRODUCT_NAME)
        print("Number of elements: ", len(all_product_name))
        for name in all_product_name:
            print(name.text)

    def results_all_product_image(self):
        all_product_image = self.driver.find_elements(*self.ALL_PRODUCT_IMAGE)
        for image in all_product_image:
            print(image.is_displayed())

    def verify_select_dept(self,category):
        locator = self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)