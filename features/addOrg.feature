

@addOrg
Feature: verify the org name and the domain is available

  Scenario: verify if the org name is available
    Given get the org name
    When hit the checkorgname API
    Then verify the availability of org name

  Scenario: verify if the domain is available
    Given get the domain name
    When hit the checkdomain API
    Then verify the availability of domain

  Scenario: verify if the user is able to upload the logo
    Given verify if the user gets the payloads
    When the user hits the api with the pay loads
    Then verify if the logo is uploaded successfully
    And the logo path is updated in the loads

  Scenario: verify if the user is able to create the organization
    Given verify if the user gets the payloads to create the Org
    When the user hits the createOrg api with the pay loads
    Then verify if the user is able to get the appkey
    And verify if the org is created

  Scenario: verify if the user is able to get the app key of the org
    Given verify if the user gets the payloads to get the app key
    When the user hits the get appkey api with the pay loads
    Then verify if the appkey is derived

  Scenario: verify if the user is able to list all org
    Given verify if the user gets the payloads to get the DB
    When the user hits the ListDB api with the pay loads
    Then verify if the DB is listed