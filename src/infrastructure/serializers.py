from src.core.entities import EventEntity, EventTypeEnum


class EventSerializer:

    def serialize(self, event_entity: EventEntity) -> dict:
        event_entity_dict = {
            "event_type": event_entity.event_type.value,
            "body": event_entity.body,
            "to": event_entity.to

        }
        return event_entity_dict

    def deserialize(self, event_entity_dict: dict) -> EventEntity:
        event_entity = EventEntity(
            event_type=EventTypeEnum(event_entity_dict.get("event_type")),
            body=event_entity_dict.get("body"),
            to=event_entity_dict.get("to")
        )
        return event_entity
