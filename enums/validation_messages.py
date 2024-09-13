from enum import Enum

class ValidationMessages(Enum):
    INVALID_FORMAT = "A part following '@' should not contain the symbol '_'."
    NO_EMAIL = "Please include an '@' in the email address. 'invalid' is missing an '@'."
    USER_NOT_EXISTS = "* Please enter a correct email address and password. Note that both fields may be case-sensitive." # div class="error-text"