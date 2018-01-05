# Created by dazzla at 03/01/2018
Feature: Polls
  # Enter feature description here

  Scenario: I can access polls
      * I am on the polls page

  Scenario: I can administer polls objects
    Given I am logged in as an administrator
    And I access polls admin

  Scenario: I can view a question
    When I am on the polls page
    Then I can access a question page