Feature: Login Page

    Background: As a user I visit the orangeHRM demo website
        Given I open the orangeHRM website
        Then I see orangeHRM login page

        Scenario: As user I do login with valid credentials
            When I do login using "valid" account
            And I click button login
            Then I success login and already in dashboard page

        Scenario: As user I do login with invalid credentials
            When I do login using "invalid" account
            And I click button login
            Then I saw error message for failed login invalid credentials

        Scenario: As user I do login with custom credentials
            When I do input username "Admin"
            And I do input password "admin123"
            And I click button login
            Then I success login and already in dashboard page
