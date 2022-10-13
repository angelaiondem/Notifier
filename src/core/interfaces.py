import abc


class BaseMessengerServiceProvider(metaclass=abc.ABC):

    @abc.abstractmethod
    def send_message(self, channel: str, body: dict) -> None:
        """Abstract method is implemented in the inherited class."""


class BaseEmailServiceProvider(metaclass=abc.ABC):
    @abc.abstractmethod
    def send_email(
            self,
            email_address: str,
            email_subject: str,
            body: str
    ) -> None:
        """
        Abstract method is implemented in the inherited class.
        """


class BaseLoggerProvider(metaclass=abc.ABC):

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
