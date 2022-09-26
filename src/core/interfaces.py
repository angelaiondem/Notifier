import abc


class BaseMessengerServiceProvider(abc.ABC):
    @abc.abstractmethod
    def send_message(self, msg_address: str, body: str) -> None:
        pass


class BaseEmailServiceProvider(abc.ABC):
    @abc.abstractmethod
    def send_email(self, email_address: str, body: str) -> None:
        pass


class BaseLoggerProvider(abc.ABC):
    @abc.abstractmethod
    def info(self, msg: str) -> None:
        pass

    @abc.abstractmethod
    def warning(self, msg: str) -> None:
        pass

    @abc.abstractmethod
    def error(self, msg: str) -> None:
        pass

    @abc.abstractmethod
    def critical(self, msg: str) -> None:
        pass
