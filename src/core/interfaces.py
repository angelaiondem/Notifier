import abc


class BaseMessengerServiceProvider(abc.ABC):

    @abc.abstractmethod
    def send_message(self, ) -> None:
        """Abstract method is implemented in the inherited class."""


class BaseEmailServiceProvider(abc.ABC):
    @abc.abstractmethod
    def send_email(
            self,
            email_address: str,
            email_subject: str,
            body: str
    ) -> None:
        """
        Abstract method is implemented in the inherited class.

        :param email_address:
        :param email_subject:
        :param body:
        :return: None
        """


class BaseLoggerProvider(abc.ABC):

    @abc.abstractmethod
    def info(self, message: str) -> None:
        """ Is implemented in the infrastructure layer."""

    @abc.abstractmethod
    def warning(self, message: str) -> None:
        """ Is implemented in the infrastructure layer."""

    @abc.abstractmethod
    def error(self, message: str) -> None:
        """ Is implemented in the infrastructure layer."""

    @abc.abstractmethod
    def critical(self, message: str) -> None:
        """ Is implemented in the infrastructure layer."""
