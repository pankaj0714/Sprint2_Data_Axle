Feature: DataAxel sprint2 search
 Scenario: search on Dataaxel search page
   Given launch Multi browser search
   When open sprint2 DataAxel search
   Then verify Movetooltip that the user search on page
   And search close browser