import logging

from pytest_bdd import scenario, given, when, then

from actions.login_pao import LoginPAO
logger = logging.getLogger(__name__)

@scenario('LoginInvalidScenarios.feature', 'User will land on login page and enters invalid credentials, validation message should be displayed to the user')
def login_invalid_credentials_test():
    logger.info("Initiating 'LoginInvalidScenarios.feature' scenarios")
    pass

@given("As user I land on login page")
def land_on_page():
    LoginPAO.land_on_login_page()

@given("As user I enter invalid suffix email value and click on submit button")
def enter_invalid_email_format_click_on_submit_button():
    LoginPAO.submit_invalid_suffix_as_user_login_details()

@when("As user I am not signed-in login has failed, verify suffix error message")
def validate_error_message_suffix():
    LoginPAO.validate_suffix_error_message()

@then("As user I enter invalid string as email value and click on submit button")
def enter_string_click_on_submit_button():
    LoginPAO.submit_string_as_user_login_details()

@then("As user I am not signed-in login has failed, verify invalid string as email error message")
def validate_error_message_suffix():
    LoginPAO.validate_string_as_error_message()
    LoginPAO.destroy_driver()

