Feature: Polls

  Scenario: I can access polls
      * I am on the polls page

  Scenario: I can administer polls objects
    When I am logged in as an administrator
    Then I access polls admin

  Scenario: I can view a question
    When I am on the polls page
    Then I can access a question page

  Scenario: Vote in poll
    When I am on a question page
    Then I can vote in a poll
