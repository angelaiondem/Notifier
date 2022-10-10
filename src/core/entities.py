from enum import Enum
from typing import Optional
from dataclasses import dataclass


@dataclass
class EnvItemEntity:
    key: str
    value: str


class EventTypeEnum(Enum):
    NEW_PUBLICATION = "new_publication"
    APPROVED_PUBLICATION = "approved_publication"


@dataclass
class EventEntity:
    event_type: EventTypeEnum
    body: str
    to: Optional[str] = None
