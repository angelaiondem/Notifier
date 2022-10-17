from email_validator import EmailNotValidError

from src import config
from src.core.entities import EventEntity
import src.core.validators as validator
from src.core.exceptions import DeserializationFailedException, \
    SerializationFailedException, InvalidEventTypeException


class EventSerializer:

    @staticmethod
    def serialize(event_entity: EventEntity) -> dict:
        event_type = event_entity.event_type
        body = event_entity.body
        to = event_entity.to
        try:
            validator.check_event_type(event_type)
            if event_type == config.APPROVED_PUBLICATION:
                validator.check_email_validation(to)
            if event_type == config.NEW_PUBLICATION:
                validator.check_string_to_dict(body)
            return {
                "event_type": event_entity.event_type,
                "body": event_entity.body,
                "to": event_entity.to
            }
        except InvalidEventTypeException as err:
            raise InvalidEventTypeException(
                err) from None  # f"Event Type is not valid:  {event_type}"
        except EmailNotValidError:
            raise EmailNotValidError(
                f"Email is not valid:  {to}"
            )
        except ValueError as err:
            raise ValueError(
                f"Slack body is not a dictionary:  {body}"
            )
        except Exception as err:
            raise SerializationFailedException("Deserialization failed", err)

    @staticmethod
    def deserialize(event_entity_dict: dict[str:str]) -> EventEntity:
        event_type = event_entity_dict.get("event_type")
        body = event_entity_dict.get("body")
        to = event_entity_dict.get("to")
        validator.check_event_type(event_type)
        try:
            if event_type == config.APPROVED_PUBLICATION:
                validator.check_email_validation(to)
            if event_type == config.NEW_PUBLICATION:
                validator.check_string_to_dict(body)
            return EventEntity(
                event_type=event_entity_dict.get("event_type"),
                body=event_entity_dict.get("body"),
                to=event_entity_dict.get("to")
            )
        except InvalidEventTypeException as err:
            # f"Event Type is not valid:  {event_type}"
            raise InvalidEventTypeException(err) from None

        except EmailNotValidError as err:  # f"Email is not valid:  {to}"
            raise EmailNotValidError(err) from None
        except ValueError as err:  # f"Slack body is not a dictionary:  {body}"
            raise ValueError(err)
        except Exception as err:  # "Deserialization failed", err
            raise DeserializationFailedException(err) from None
