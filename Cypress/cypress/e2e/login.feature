Feature: Login Page

    Scenario: As user I do login with valid credentials
        Given I open the orangeHRM website
        When I do login using "valid" account
        And I click button login
        Then I success login and already in dashboard page

    Scenario: As user I do login with invalid credentials
        Given I open the orangeHRM website
        When I do login using "invalid" account
        And I click button login
        Then I saw error message for failed login invalid credentials

    Scenario: As user I do login with custom credentials
        Given I open the orangeHRM website
        When I do input username "Admin"
        And I do input password "admin123"
        And I click button login
        Then I success login and already in dashboard page