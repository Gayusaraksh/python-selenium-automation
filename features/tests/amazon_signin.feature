# Created by gayathri at 2/12/23
Feature: Amazon sign in tests

  Scenario: User can see Amazon signin page
    Given Open Amazon page
    When Click on Orders button
    Then Verify that the Sign in header is visible in sign in page
    And Verify that Email or mobile phone number label is present in sign in page
    And Verify that the Email input field is present in sign in page