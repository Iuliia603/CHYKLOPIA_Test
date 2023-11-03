Feature: Header functionality
  In order to navigate through the website, the user should be able to access different directions from the header.

  Background:
    Given user opens the Homepage


  Scenario: Open Capabilities page

    When user clicks the "Capabilities" button
    Then Capabilities page is open


  Scenario: Open Brand Strategy & Development from the "Capabilities" dropdown

    When user clicks the "Capabilities" dropdown
    And user clicks "Brand Strategy & Development"
    Then Brand Strategy & Development page is open

  Scenario: Open Brand Strategy & Development from the hovering over the "Capabilities" dropdown
    When user hovers the cursor over the "Capabilities" dropdown
    And the Capabilities" options are displayed
    And user clicks "Brand Strategy & Development"
    Then Brand Strategy & Development page is open

  Scenario: Open Growth Support page

    When user clicks the "Growth Support" button
    Then Growth Support page is open


  Scenario: Open Work page

    When user clicks the "Work" button
    Then Work page is open


  Scenario: Button "Get on a call" functionality

    When user clicks the "Get on a call" button
    Then The page for booking a call is open


