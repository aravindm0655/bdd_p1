

@roles
Feature: Roles Management

  Scenario: Verify if the user can add a new role
    Given the user has the payload to add a role
    When the user hits the addRole API
    Then the added role should be done correctly

  Scenario: Verify if the user can view all the designations
    Given the user has the payload to view the role
    When the user hits the listRole API
    Then the added role should be listed