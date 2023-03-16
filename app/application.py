from pages.header import Header
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.terms_conditions_page import TermsConditionsPage
from pages.privacy_notice_page import PrivacyNoticePage
from pages.customer_service_page import CustomerServicePage


class Application:

    def __init__(self,driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.terms_conditions_page = TermsConditionsPage(self.driver)
        self.privacy_notice_page = PrivacyNoticePage(self.driver)
        self.customer_service_page = CustomerServicePage(self.driver)
