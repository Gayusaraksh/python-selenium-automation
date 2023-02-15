# Created by gayathri at 2/14/23
Feature: Amazon cart tests

  Scenario: User can see Amazon cart page
    Given Open Amazon page
    When Click on cart icon
    Then Verify that Your Amazon Cart is empty is shown in the cart page
