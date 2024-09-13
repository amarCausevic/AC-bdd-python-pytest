import logging
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from common.config_utils import ConfigUtils
from common.driver_utils import DriverUtils
from common.element_utils import ElementUtils
from common.selector_utils import SelectorUtils
from common.wait_utils import WaitUtils
from enums.selectors_path import SelectorsPath
from enums.validation_messages import ValidationMessages

logger = logging.getLogger(__name__)

class LoginPAO:
  _driver: WebDriver
  _username_whole_string: str = ConfigUtils.get_property("InvalidCredentials", "username_whole_string")
  _username_suffix: str = ConfigUtils.get_property("InvalidCredentials", "username_suffix")
  _password: str = ConfigUtils.get_property("InvalidCredentials", "password")

  @staticmethod
  def page_prerequisites() -> WebDriver:
    _url: str = ConfigUtils.get_property("Workspace", "url")

    LoginPAO._driver = DriverUtils.create_driver()
    LoginPAO._driver.get(_url)
    return LoginPAO._driver

  @staticmethod
  def land_on_login_page():
    LoginPAO.page_prerequisites()
    WaitUtils.wait_for_element(SelectorsPath.LOGIN_LEFT_SIDE_CONTAINER.value, LoginPAO._driver)

  @staticmethod
  def submit_user_login_details(username: str, password:str):
    _username_input: WebElement = SelectorUtils.get_element(LoginPAO._driver, SelectorsPath.INPUT_USERNAME.value)
    _password_input: WebElement = SelectorUtils.get_element(LoginPAO._driver, SelectorsPath.INPUT_PASSWORD.value)
    _submit_button: WebElement = SelectorUtils.get_element(LoginPAO._driver, SelectorsPath.BUTTON_SUBMIT.value)

    ElementUtils.clear_input(_username_input)
    ElementUtils.clear_input(_password_input)
    ElementUtils.send_keys(_username_input, username)
    ElementUtils.send_keys(_password_input, password)
    _submit_button.click()

  @staticmethod
  def validate_error_message(expected_error_message):
    logger.info("This is current: " + WaitUtils.wait_and_retrieve_validation_message(SelectorsPath.INPUT_USERNAME.value, LoginPAO._driver))
    logger.info("This is expected: " + expected_error_message)
    assert WaitUtils.wait_and_retrieve_validation_message(SelectorsPath.INPUT_USERNAME.value, LoginPAO._driver) == expected_error_message

  @staticmethod
  def destroy_driver():
    LoginPAO._driver.close()

  @staticmethod
  def submit_string_as_user_login_details():
    LoginPAO.submit_user_login_details(LoginPAO._username_whole_string, LoginPAO._password)

  @staticmethod
  def submit_invalid_suffix_as_user_login_details():
    LoginPAO.submit_user_login_details(LoginPAO._username_suffix, LoginPAO._password)

  @staticmethod
  def validate_suffix_error_message():
    LoginPAO.validate_error_message(ValidationMessages.INVALID_FORMAT.value)
    SelectorUtils.get_element(LoginPAO._driver, SelectorsPath.LOGIN_LEFT_SIDE_CONTAINER.value).click()

  @staticmethod
  def validate_string_as_error_message():
    LoginPAO.validate_error_message(ValidationMessages.NO_EMAIL.value)
