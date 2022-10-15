import abc
from typing import Optional

from src import config
from src.core.use_cases import NotifierUseCase
from src.infrastructure.providers import EmailServiceProvider, LoggerProvider, \
    SlackMessengerProvider
from src.infrastructure.repositories import ConfigRepo
from src.infrastructure.serializers import EventSerializer
from src.infrastructure.services import EmailService, LoggerService, \
    SlackService


class BaseController(abc.ABC):

    def __init__(self):
        self._slack_service: Optional[SlackService] = None
        self._email_service: Optional[EmailService] = None
        self._logg_service: Optional[LoggerService] = None
        self._env_repo: Optional[ConfigRepo] = None
        self._messenger_service_provider: Optional[
            SlackMessengerProvider] = None
        self._email_provider: Optional[EmailServiceProvider] = None
        self._logger_service_provider: Optional[LoggerProvider] = None

    @property
    def slack_service(self) -> SlackService:
        if self._slack_service is None:
            self._slack_service = SlackService(
                slack_token=self.env_repo.get_one(config.SLACK_TOKEN).value,
                slack_channel=config.SLACK_CHANNEL
            )
        return self._slack_service

    @property
    def email_service(self) -> EmailService:
        """
        Check, create and return the EmailService object instance.
        :return: EmailService object.
        """
        if self._email_service is None:
            self._email_service = EmailService(
                smtp_host=self.env_repo.get_one(config.SMTP_HOST).value,
                smtp_port=self.env_repo.get_one(config.SMTP_PORT).value,
                email_username=self.env_repo.get_one(
                    config.EMAIL_USERNAME).value,
                email_app_pass=self.env_repo.get_one(
                    config.EMAIL_APP_PASS).value,
                from_email=self.env_repo.get_one(config.FROM_EMAIL).value,
                email_subject=config.EMAIL_SUBJECT
            )
        return self._email_service

    @property
    def logger_service(self):
        if self._logg_service is None:
            self._logg_service = LoggerService(
                logger_name=config.LOGGER_NAME,
                formatter=config.DEFAULT_LOG_FORMAT,
                log_file_path=config.LOG_FILE_PATH,
                log_level=config.DEFAULT_LOG_LEVEL
            )
        return self._logg_service

    @property
    def env_repo(self):
        if self._env_repo is None:
            self._env_repo = ConfigRepo()
        return self._env_repo

    @property
    def email_service_provider(self):
        if self._email_provider is None:
            self._email_provider = EmailServiceProvider(
                self.logger_service_provider,
                self.email_service
            )
        return self._email_provider

    @property
    def messenger_service_provider(self) -> SlackMessengerProvider:
        if self._messenger_service_provider is None:
            self._messenger_service_provider = SlackMessengerProvider(
                self.logger_service_provider, self.slack_service
            )
        return self._messenger_service_provider

    @property
    def logger_service_provider(self):
        if self._logger_service_provider is None:
            self._logger_service_provider = LoggerProvider(self.logger_service)
        return self._logger_service_provider


class APIController(BaseController):

    def process_event(self, request_data: dict):
        # TODO check validations.
        event_entity = EventSerializer.deserialize(request_data)
        if event_entity.event_type == "new_publication":
            notifier_use_case = NotifierUseCase(
                event_entity,
                self.messenger_service_provider
            )
            notifier_use_case.execute()
        elif event_entity.event_type == "approved_publication":
            notifier_use_case = NotifierUseCase(
                event_entity,
                self.email_service_provider
            )
            notifier_use_case.execute()
