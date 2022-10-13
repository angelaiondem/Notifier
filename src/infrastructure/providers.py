import logging

import src.core.interfaces as sci
import src.infrastructure.services as sis
from src import config


class SlackMessengerProvider(sci.BaseMessengerServiceProvider):

    def __init__(
            self,
            logger_provider: sci.BaseLoggerProvider,
            slack_service: sis.SlackService
    ):
        self._logger_provider = logger_provider
        self._slack_service = slack_service

    def send_message(self,  channel: str, body: str) -> None:
        """
        Post a message(body) to a given channel.
        """
        self._slack_service.send_message(channel=channel, body=body)


class EmailServiceProvider(sci.BaseEmailServiceProvider):

    def __init__(
            self,
            logger_provider: sci.BaseLoggerProvider,
            email_service: sis.EmailService
    ):
        self._logger_provider = logger_provider
        self._email_service = email_service

    def send_email(
            self,
            email_address: str,
            email_subject: str,
            body: str
    ) -> None:
        self._email_service.send_email(email_address, email_subject, body)


class LoggerProvider(sci.BaseLoggerProvider):

    def __init__(self, logger_service: sis.LoggerService):
        self.logger_service = logger_service

    @property
    def logger(self):
        logger = logging.Logger(name=self.logger_name)
        logger.setLevel(self.log_level)
        file_handler = logging.FileHandler(self.log_file_path)
        formatter = logging.Formatter(self.log_format)
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
