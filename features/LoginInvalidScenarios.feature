Feature: User lands on Joan Workspace Login page and enters invalid credentials with different scenarios
    Scenario: User will land on login page and enters invalid credentials, validation message should be displayed to the user
        Given As user I land on login page
        And As user I enter invalid suffix email value and click on submit button
        When As user I am not signed-in login has failed, verify suffix error message
        Then As user I enter invalid string as email value and click on submit button
        And As user I am not signed-in login has failed, verify invalid string as email error message