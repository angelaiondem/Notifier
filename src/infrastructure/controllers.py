import abc
import json

import requests

import src.config as conf
from src.infrastructure.providers import EmailServiceProvider, LoggerProvider
from src.infrastructure.repositories import ConfigRepo
from src.infrastructure.services import EmailService, LoggerService


class BaseController(abc.ABC):
    _email_service: EmailService
    _logg_service: LoggerService
    _env_repo: ConfigRepo
    _email_provider: EmailServiceProvider
    _logger_service_provider: LoggerProvider


    def slack_service(self):
        pass

    @property
    def email_service(self) -> EmailService:
        """
        Check, create and return the EmailService object instance.
        :return: EmailService object.
        """
        if self._email_service is None:
            self._email_service = EmailService(
                smtp_host=self._env_repo.get_one(conf.SMTP_HOST).value,
                smtp_port=self._env_repo.get_one(conf.SMTP_PORT).value,
                email_username=self._env_repo.get_one(
                    conf.EMAIL_USERNAME).value,
                email_app_pass=self._env_repo.get_one(
                    conf.EMAIL_APP_PASS).value,
                from_email=self._env_repo.get_one(conf.FROM_EMAIL).value

            )
        return self._email_service

    @property
    def logger_service(self):
        if self._logg_service is None:
            self._logg_service = LoggerService(
                logger_name=conf.LOGGER_NAME,
                formatter=conf.DEFAULT_LOG_FORMAT,
                log_file_path=conf.LOG_FILE_PATH,
                log_level=conf.DEFAULT_LOG_LEVEL
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
    def messenger_service_provider(self):
        pass

    @property
    def logger_service_provider(self):
        if self._logger_service_provider is None:
            self._logger_service_provider = LoggerProvider(self.logger_service)
        return self._logger_service_provider


class APIController(BaseController):

    def process_event(self, event: json):
        if event["event_type"] == "new_publication":
            send_message = B
