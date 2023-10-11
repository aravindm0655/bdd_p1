@package_feature
Feature: package feature Management

  Scenario: Verify if the user can create a new package feature
    Given the user has the payload to create package feature
    When the user hits the createpackage_feature API
    Then the creation of the package feature must be done correctly

  Scenario: Verify if the user can view all the package feature
    Given the user has the payload to view the package feature
    When the user hits the getpackagefeatures API
    Then the packages feature must be listed

  Scenario: Verify if the user can view package with id
    Given the user gets the id to view the package feature
    When the user hits the getpackagefeatures_by_id API
    Then the added package package should be displayed