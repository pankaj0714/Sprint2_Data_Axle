Feature: DataAxel Login
 Scenario: Login on Dataaxel login page
   Given launch chrome browser
   When open DataAxel Login
   Then verify that the user login on page
   And close browser