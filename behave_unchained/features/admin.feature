Feature: Admin

  Scenario: I can administer polls objects
    When I am logged in as an administrator
    Then I can access polls admin

  Scenario: I can administer questions objects
    Given I am logged in as an administrator
    And I can access questions admin