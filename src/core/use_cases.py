import abc
from typing import Union

from src.core.entities import EventEntity
from src.infrastructure.providers import SlackMessengerProvider, \
    EmailServiceProvider
from src.infrastructure.serializers import EventSerializer


class BaseUseCase(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass


class NotifierUseCase(BaseUseCase):

    def __init__(
            self,
            event_entity: EventEntity,
            service_provider: Union[
                SlackMessengerProvider, EmailServiceProvider]
    ):
        self.event_entity = event_entity
        self.event_entity_dict = EventSerializer.serialize(event_entity)
        self.service_provider = service_provider

    def execute(self):
        if isinstance(self.service_provider, SlackMessengerProvider):
            self.service_provider.send_message(
                event_entity=self.event_entity_dict
            )
        if isinstance(self.service_provider, EmailServiceProvider):
            self.service_provider.send_email(
                event_entity=self.event_entity
            )
