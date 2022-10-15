from src.core.entities import EventEntity


class EventSerializer:

    @staticmethod
    def serialize(event_entity: EventEntity) -> dict:
        event_entity_dict = {
            "event_type": event_entity.event_type,
            "body": event_entity.body,
            "to": event_entity.to

        }
        return event_entity_dict

    @staticmethod
    def deserialize(event_entity_dict: dict) -> EventEntity:
        event_entity = EventEntity(
            event_type=event_entity_dict.get("event_type"),
            body=event_entity_dict.get("body"),
            to=event_entity_dict.get("to")
        )
        return event_entity
