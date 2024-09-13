from selenium.webdriver.remote.webelement import WebElement


class ElementUtils:

  @staticmethod
  def send_keys(element: WebElement, value:str):
    element.send_keys(value)

  @staticmethod
  def clear_input(element: WebElement):
    element.clear()