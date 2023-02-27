# Created by gayathri at 2/14/23
Feature: Amazon adding items to cart tests

  Scenario: User can add items to the cart.
    Given Open Amazon page
    When Enter Handbags in the search box
    And Click on search icon
    And Select item from the search list
    And Click on Add to cart
    And Click on cart icon
    Then Check for 1 item in the cart