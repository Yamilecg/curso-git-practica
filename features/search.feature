Feature: ITESO Website Search
  As a prospective student
  I want to search for "carreras" on the ITESO homepage
  So that I can see the study programs offered by the university

  Scenario: Searching for study programs on ITESO website
    Given I am on the ITESO homepage
    When I search for "carreras"
    Then I should see results related to ITESO study programs
