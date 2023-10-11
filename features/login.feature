
@login

Feature: Login feature

  Scenario: verify if the user can able to login with correct credential
    Given the user has the correct credential to login
    When the user hit the api with correct credential
    Then the user must be logged in

  Scenario Outline: verify if the user cannot login with wrong credential
    Given the user has the incorrect <username> and <password>
    When the user hit the api with wrong credential
    Then the user must not be logged in

    Examples:
      | username | password   |
      | admin    | !@#$%^&*(  |
      | !@#$%^   | wrongpass2 |
      | user3    | wrongpass3 |
      | user1    | wrongpass1 |
      | user1    | wrongpass1 |
      | user2    | wrongpass2 |
      | user3    | wrongpass3 |