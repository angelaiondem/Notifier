import src.core.interfaces as sci


class SlackMessengerProvider(sci.BaseMessengerServiceProvider):

    def send_message(self, msg_address: str, body: str) -> None:
        pass


class EmailServiceProvider(sci.BaseEmailServiceProvider):

    def send_email(self, email_address: str, body: str) -> None:
        pass


class LoggerProvider(sci.BaseLoggerProvider):

    def info(self, msg: str) -> None:
        pass

    def warning(self, msg: str) -> None:
        pass

    def error(self, msg: str) -> None:
        pass

    def critical(self, msg: str) -> None:
        pass
