# Created by gayathri at 3/23/2023
Feature: Amazon main page tests

  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify spanish option present


  Scenario: User can see the deals
    Given Open amazon product page gp/product/B074TBCSC8
    When Hover over new arrivals
    Then Verify user sees the deals
