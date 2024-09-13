from enum import Enum

class SelectorsPath(Enum):
    BUTTON_SUBMIT = ".//button[@type='submit']"
    INPUT_USERNAME = ".//input[@placeholder='email@address.com']"
    INPUT_PASSWORD = ".//input[@placeholder='Password']"
    LOGIN_LEFT_SIDE_CONTAINER = ".//div[contains(@class, 'auth-signin-left-textbox')]"
