import logging

from src.core.interfaces import BaseMessengerServiceProvider, \
    BaseLoggerProvider, BaseEmailServiceProvider
from src.infrastructure.services import SlackService, LoggerService, \
    EmailService
from src.core.entities import EventEntity


class SlackMessengerProvider(BaseMessengerServiceProvider):

    def __init__(
            self,
            logger_provider: BaseLoggerProvider,
            slack_service: SlackService
    ):
        self._logger_provider = logger_provider
        self._slack_service = slack_service

    def send_message(self, event_entity: dict) -> None:
        """
        Post a message(body) to a given slack channel.
        """
        self._slack_service.send_message(event_entity=event_entity)


class EmailServiceProvider(BaseEmailServiceProvider):

    def __init__(
            self,
            logger_provider: BaseLoggerProvider,
            email_service: EmailService
    ):
        self._logger_provider = logger_provider
        self._email_service = email_service

    def send_email(self, event_entity: EventEntity) -> None:
        self._email_service.send_email(event_entity)


class LoggerProvider(BaseLoggerProvider):

    def __init__(self, logger_service: LoggerService):
        self._logger_service = logger_service

    @property
    def logger(self):
        logger = logging.Logger(name=self._logger_service.logger_name)
        logger.setLevel(self._logger_service.log_level)
        file_handler = logging.FileHandler(self._logger_service.log_file_path)
        formatter = logging.Formatter(self._logger_service.log_format)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def info(self, message: str) -> None:
        return self.logger.info(message)

    def warning(self, message: str) -> None:
        return self.logger.warning(message)

    def error(self, message: str) -> None:
        return self.logger.error(message)

    def critical(self, message: str) -> None:
        return self.logger.critical(message)
