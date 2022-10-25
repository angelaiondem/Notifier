import logging
from logging import Logger, FileHandler, Formatter

from src import config
from src.core.exceptions import SlackMessageIsNotSentException, \
    EmailIsNotSentException
from src.core.interfaces import BaseMessengerServiceProvider, \
    BaseLoggerProvider, BaseEmailServiceProvider
from src.infrastructure.services import SlackService, LoggerService, \
    EmailService
from src.core.entities import EventEntity


class SlackMessengerProvider(BaseMessengerServiceProvider):

    def __init__(
            self,
            logger_service_provider: BaseLoggerProvider,
            slack_service: SlackService
    ):
        self._logger_service_provider = logger_service_provider
        self._slack_service = slack_service

    def send_message(self, event_entity: EventEntity) -> None:
        """
        POST/Send a message(body) to a defined slack channel.
        """
        try:
            self._slack_service.send_message(event_entity=event_entity)
            self._logger_service_provider.info(
                f"Slack message is sent. ID: {config.SLACK_CHANNEL_ID}")
        except SlackMessageIsNotSentException as err:
            self._logger_service_provider.error(
                f"Failed to send slack message. ID: {config.SLACK_CHANNEL_ID}")
            raise SlackMessageIsNotSentException(err) from None


class EmailServiceProvider(BaseEmailServiceProvider):

    def __init__(
            self,
            logger_service_provider: BaseLoggerProvider,
            email_service: EmailService
    ):
        self._logger_service_provider = logger_service_provider
        self._email_service = email_service

    def send_email(self, event_entity: EventEntity) -> None:
        """
        POST/Send a message to a given email address.
        :param event_entity:
        :return None:
        """
        try:
            self._email_service.send_email(event_entity)
            self._logger_service_provider.info(
                f"Email is sent. Address: {event_entity.to}")
        except EmailIsNotSentException as err:
            self._logger_service_provider.error(
                f"Failed to send an email. Address: {event_entity.to}")
            raise EmailIsNotSentException(err) from None


class LoggerServiceProvider(BaseLoggerProvider):

    def __init__(self, logger_service: LoggerService):
        self._logger_service = logger_service

    @property
    def logger(self) -> Logger:
        """
        Set the logger and the handler parameters.
        :return:
        """
        logger = logging.getLogger(name=self._logger_service.logger_name)
        logger.setLevel(self._logger_service.log_level)
        file_handler = FileHandler(self._logger_service.log_file_path)
        formatter = Formatter(self._logger_service.log_format)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)
