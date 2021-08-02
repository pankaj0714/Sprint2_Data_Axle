Feature: DataAxel sprint1 Login
 Scenario: Signin on Dataaxel login page
   Given launch sprint1 chrome browser
   When open sprint1 DataAxel signin
   Then verify sprint1 that the user signin on page
   And sprint1login close browser