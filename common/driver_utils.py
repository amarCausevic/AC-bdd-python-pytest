from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.ie.webdriver import WebDriver


class DriverUtils:
  _driver = None
  _options:ChromiumOptions = webdriver.ChromeOptions()

  @staticmethod
  def add_chrome_options() -> ChromiumOptions:
    DriverUtils._options.add_argument("--start-incognito")
    DriverUtils._options.add_argument("--start-maximized")
    DriverUtils._options.add_argument("--no-default-browser-check")
    DriverUtils._options.add_argument("--search-engine-choice-country")
    return DriverUtils._options

  @staticmethod
  def create_driver() -> WebDriver:
    DriverUtils._driver = webdriver.Chrome(options=DriverUtils.add_chrome_options())
    return DriverUtils._driver
