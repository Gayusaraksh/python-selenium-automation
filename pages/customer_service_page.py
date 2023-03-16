from pages.base_page import Page
from selenium.webdriver.common.by import By


class CustomerServicePage(Page):
    WELCOME_TEXT = (By.XPATH, '//h1[text()="Welcome to Amazon Customer Service"]')
    CARD_CONTAINER = (By.CSS_SELECTOR, 'div.issue-card-container')
    SEARCH_HELP_LIBRARY = (By.XPATH, '//h2[text()="Search our help library"]')
    QUESTIONS_INPUT_FIELD = (By.CSS_SELECTOR, 'input#hubHelpSearchInput')
    ALL_HELP_TOPICS = (By.XPATH, '//h2[text()="All help topics"]')
    RECOMMENDED_TOPICS = (By.CSS_SELECTOR, 'ul.help-topics')

    def verify_welcome_text(self,expected_text):
        self.verify_text(expected_text,*self.WELCOME_TEXT)

    def verify_card_container(self):
        self.verify_if_displayed(*self.CARD_CONTAINER)

    def verify_search_help_library(self,expected_text):
        self.verify_text(expected_text,*self.SEARCH_HELP_LIBRARY)

    def verify_search_query_field(self):
        self.verify_if_displayed(*self.QUESTIONS_INPUT_FIELD)

    def verify_all_help_topics(self,expected_text):
        self.verify_text(expected_text,*self.ALL_HELP_TOPICS)

    def verify_recommended_topics(self):
        self.verify_if_displayed(*self.RECOMMENDED_TOPICS)



