from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class SelectorUtils:

  @staticmethod
  def get_element(driver: WebDriver, xPath:str) -> WebElement:
    return driver.find_element(By.XPATH,xPath)