# Created by mdAbdulWahid at 2019-03-30
Feature: Forms
  @forms
  Scenario: Empty form validation
    Given the user is taken to the form page
    When the user presses the submit button without inserting anything
    Then the alert message should be shown

  Scenario: Directs to next page
    Given the user is taken to the form page and fills in the details
    When the user presses the submit button
    Then the user should see the pictures of 3 cats

