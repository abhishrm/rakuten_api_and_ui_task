@ui_youtube_test
Feature: UI: youtube
description
This feature file contain test related to youtube ui (UI test automation, Python)

# Verify all the below test with respect to different browsers. In order to test it on browser like Firefox,Edge.
#Please set the variable "browser_to_use" placed in commonconfig.ini (located under path steps/config/commonconfig.ini)to respective browser
# on which you want to run test. By default this parameter is set to Chrome, so all test will run on chrome brwoser by default


@TC-1 @ui
Scenario: UI- Verify user can login to youtube and search content .

When user has navigated to the youtube landing page
Then user can locate the sign in button and then can "click" it
Then user can verify that the login username screen appears
#
When user send the text to the username field as "username" and click "next"
Then user can verify that the login password screen appears
#
When user send the text to the password field as "password" and click "next"
And user looks for text "hollywood trailors" on youtube serach page and then click it
Then user can see the search result and verify it


@TC-2 @ui
Scenario Outline: UI- Verify user "can not" login to youtube app with wrong_username/empty_username/username_with_leading_spaces/username_with_trailing_spaces.

When user has navigated to the youtube landing page
Then user can locate the sign in button and then can "click" it
Then user can verify that the login username screen appears
#
When user send the text to the username field as "<username>" and click "next"
Then user can see login failed with text "<text>"

Examples: username type
| username |     text |

| wrong_username | Couldn’t find your Google Account|
|        empty_username        | Enter an email or phone number. |
|   username_with_leading_spaces             |Couldn’t find your Google Account|
|      username_with_trailing_spaces          |Couldn’t find your Google Account|

@TC-3 @ui
Scenario Outline: UI- Verify user can not login to youtube app with wrong password/empty_password/password_with_leading_spaces/password_with_trailing_spaces.

When user has navigated to the youtube landing page
Then user can locate the sign in button and then can "click" it
Then user can verify that the login username screen appears
#
When user send the text to the username field as "username" and click "next"
Then user can verify that the login password screen appears

When user send the text to the password field as "<password>" and click "next"
Then user can see password failed with text "<text>"

Examples: passwordverify
| password |text|

| wrong_password | Wrong password |
|        empty_password        | Enter a password |
|   password_with_leading_spaces             | Wrong password |
|      password_with_trailing_spaces          |Wrong password |


#@TC-4
## Verify all the above test with respect to different browsers. In order to test it on browser like Firefox,Edge.
#Please set the variable "browser_to_use" placed in commonconfig.ini (located under path steps/config/commonconfig.ini)to respective browser
# on which you want to run test. By default this parameter is set to Chrome, so all test will run on chrome brwoser by default