

@desi
Feature: Designation Management

  Scenario: Verify if the user can add the designation
    Given the user has the payload to add a designation
    When the user hits the addDes API
    Then the added designation should be done correctly

  Scenario: Verify if the user can view all the designations
    Given the user has the payload to view designations
    When the user hits the listDes API
    Then the added designation should be listed
