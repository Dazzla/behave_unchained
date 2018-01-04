# Created by dazzla at 03/01/2018
Feature: Polls
  # Enter feature description here

  Scenario: I can access polls
    Given I am on the polls page
    Then I can see the text 'Hello, world. You're at the polls index.'

  Scenario: I can administer questions
    Given I am logged in as an administrator
    Given I access 'polls/question' admin