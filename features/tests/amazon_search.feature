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


  Scenario: User can click through product colors.
    Given Open Amazon page
    When Enter Handbags in the search box
    And Click on search icon
    And Select item from the search list
    Then Verify user can click through colors


  Scenario: User can see product name for every product on amazon search results.
    Given Open Amazon page
    When Enter coffee in the search box
    And Click on search icon
    Then Verify that every product on Amazon search results page has product name
    And Verify that every product on Amazon search results page has product image


  Scenario: User can select and search in a department.
    Given Open Amazon page
    When Select department by alias amazonfresh
    When Enter Cucumber in the search box
    When Click on search icon
    Then Verify amazonfresh department is selected