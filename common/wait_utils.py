
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WaitUtils:
  _wait: WebDriverWait

  @staticmethod
  def wait_and_retrieve_validation_message(element: str, driver: WebDriver) -> str:
    return WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, element))).get_attribute("validationMessage")

  @staticmethod
  def wait_for_element(element: str, driver: WebDriver) -> WebElement:
    return WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, element)))