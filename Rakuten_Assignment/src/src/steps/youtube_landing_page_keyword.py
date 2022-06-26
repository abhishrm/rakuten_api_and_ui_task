from behave import *
import src.steps.UI.cat_landing_page_ops as cat_landing_page
from src.steps.common.common_ui_utility import *
import re
_module = os.path.basename(__file__)



@when('user has navigated to the youtube landing page')
@Then('user can locate the sign in button and then can "{click}" it')
def step_impl(context,click=None):
    """
    Keyword implemenation to locate signin youtube button
    :param context:
    :param click:click need to be performed
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._locate_and_click_sign_in_button(click), 'locating signin button failed'.format(attribute)

@when('user send the text to the username field as "{username}" and click "{next_button}"')
@then('user can verify that the login username screen appears')
def step_impl(context, username=None,next_button =None):
    """
    Keyword implemenation to find the username section and send username details
    :param context:
    :param username:username text to be provided.
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)
    if username is not None and next_button is None:
        if username == 'wrong_username':
            username = context.wrong_username
        elif username == 'empty_username':
            username = ""
        elif username == 'username_with_leading_spaces':
            username =  "     " + context.username
        elif username == 'username_with_trailing_spaces':
            username = context.username + "    "
        else:
            username = context.username

    assert landing_page._locate_verify_username_login_window(username,next_button), 'sending/verifying in username text field failed'.format(attribute)

@when('user user send the text to the password field as "{password}" and click "{next_button}"')
@then('user can verify that the login password screen appears')
def step_impl(context, password=None,next_button=None):
    """
    Keyword implemenation to send the password
    :param context:
    :param password:password to be provided
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)
    if password is not None:

        if password == 'wrong_password':
            password = context.wrong_password
        elif password == 'empty_password':
            password = ""
        elif password == 'password_with_leading_spaces':
            password = "     " + context.password
        elif password == 'password_with_trailing_spaces':
            password = context.password + "    "
        else:
            password = context.password

    assert landing_page._locate_verify_password_login_window(password,next_button), 'Verifying/sending password in password field failed'.format(attribute)


@when('user looks for text "{search_text}" on youtube serach page and then click it')
def step_impl(context, search_text):
    """
    keyword implementation to search on youtube by user provided input
    :param context:
    :param attribute:searchbox on landimg page
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)
    context.search_text = search_text

    assert landing_page._get_search_box_and_then_click_it(search_text), 'Search operation failed '

@when('user can see the search result and verify it')
def step_impl(context):
    """
    keyword implementation to verify end result of search operation
    :param context:
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._verify_search_result(result), 'Search and click to : {} failed '.format(attribute)

@then('user can see login failed with text "{text}"')
def step_impl(context, text):
    """
    Keyword implemenation to verify login failure due to wrong username.
    :param context:
    :param text:error text to look for.
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._verify_username_failure_text(text), 'Verifying wrong username failure, failed'.format(attribute)


@then('user can see password failed with text "{text}"')
def step_impl(context, text):
    """
    Keyword implemenation to verify password failure due to wrong password.
    :param context:
    :param text:error text to look for.
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._verify_password_failure_text(text), 'Verifying wrong password failure ,failed'.format(attribute)



