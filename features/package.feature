@package
Feature: package Management

  Scenario: Verify if the user can create a new package
    Given the user has the payload to create package
    When the user hits the createpackage API
    Then the creation of the package must be done correctly

  Scenario: Verify if the user can view all the package
    Given the user has the payload to view the package
    When the user hits the getpackages API
    Then the packages must be listed

  Scenario: Verify if the user can view package with id
    Given the user gets the id to view the package
    When the user hits the getpackages_by_id API
    Then the added package should be displayed