# Created by gayathri at 2/26/23
Feature: BestSellers page link tests

  Scenario: User can see 5 links on Bestsellers page.
    Given Open Amazon page
    When Click on Best Sellers link
    Then Verify 5 links are present on the Best Sellers page
    Then Click on each top links and check correct page opened
