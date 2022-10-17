from email_validator import validate_email, EmailNotValidError

from src import config
from src.core.exceptions import InvalidEventTypeException


def check_email_validation(email_address: str) -> bool:
    """
    Check if the email address is valid.
    :param email_address:
    :return: boolean
    """
    try:
        if validate_email(email_address, timeout=3).email:
            print("email is true")
            return True
        else:
            raise EmailNotValidError
    except EmailNotValidError as err:
        raise EmailNotValidError(err) from None
    except Exception as err:
        raise EmailNotValidError(err) from None


def check_event_type(event_type: str) -> bool:
    """
    Check if the event type is one of the defined types.
    :param event_type:
    :return boolean:
    """
    if event_type in [config.NEW_PUBLICATION, config.APPROVED_PUBLICATION]:
        return True
    else:
        raise InvalidEventTypeException


def check_string_to_dict(slack_body: str) -> bool:
    """
    Check is the given string is a dictionary.
    :param slack_body:
    :return boolean:
    """
    try:
        dict(slack_body)
        return True
    except ValueError as err:
        raise ValueError(err) from None
