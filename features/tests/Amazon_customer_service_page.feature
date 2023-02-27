# Created by gayathri at 2/26/23
Feature: Amazon customer service page

  Scenario: User can see "Welcome to Amazon Customer Service" on the customer service page.
    Given Open Amazon page
    When Click on Customer Service link
    Then Check Welcome to Amazon Customer Service text is present on the page


  Scenario: User can see "Table of contents" on the customer service page.
    Given Open Amazon page
    When Click on Customer Service link
    Then Check Table of contents present on the page


  Scenario: User can see "Search our help library" on the customer service page.
    Given Open Amazon page
    When Click on Customer Service link
    Then Check Search our help library is present on the page


  Scenario: User can see "Questions about charge input box" on the customer service page.
    Given Open Amazon page
    When Click on Customer Service link
    Then Check Search box shown in the page


  Scenario: User can see "All help topics" on the customer service page.
    Given Open Amazon page
    When Click on Customer Service link
    Then Check All help topics present on the page


  Scenario: User can see "Recommended Topics" on the customer service page.
    Given Open Amazon page
    When Click on Customer Service link
    Then Check Recommended Topics present on the customer service page