from email_validator import EmailNotValidError

from src import config
from src.core.entities import EventEntity
import src.core.validators as validator
from src.core.exceptions import DeserializationFailedException, \
    SerializationFailedException, InvalidEventTypeException


class EventSerializer:

    @staticmethod
    def serialize(event_entity: EventEntity) -> dict:
        """
        Based on the given EventEntity class data, check all data values and,
        return a dictionary type data.
        :param event_entity:
        :return dict:
        """
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
            raise InvalidEventTypeException(err) from None
        except EmailNotValidError as err:
            raise EmailNotValidError(err) from None
        except ValueError as err:
            raise ValueError(err) from None
        except Exception as err:
            raise SerializationFailedException(err) from None

    @staticmethod
    def deserialize(event_entity_dict: dict[str:str]) -> EventEntity:
        """
        Based on the given dictionary type data, check all data values and,
        return an EventEntity type object.
        :param event_entity_dict:
        :return EventEntity:
        """
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
            raise InvalidEventTypeException(err) from None
        except EmailNotValidError as err:
            raise EmailNotValidError(err) from None
        except ValueError as err:
            raise ValueError(err)
        except Exception as err:
            raise DeserializationFailedException(err) from None
