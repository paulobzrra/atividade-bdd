Feature: PLatform

  Scenario: View Shortcuts
    Given the platform site is running
    When the user select to view shortcuts
    Then platform shows the shortcuts

 Scenario: Help
    Given platform is running
    When the user select help
    Then platform shows the help center

  Scenario: Zoom in the letters
    Given platform site is running
    When the user select increase font size in acessibility menu
    Then the letters in the screen grow up


