# Created by dazzla at 03/01/2018
Feature: Polls
  # Enter feature description here

  Scenario: I can access polls
    * I can see the text 'Hello, world. You're at the polls index.' on the polls page

  Scenario: I can administer objects
    Given I am logged in as an administrator
    And I access object admin