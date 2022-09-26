import src.infrastructure.providers as sip


class EmailService(sip.EmailServiceProvider):
    pass


class SlackService(sip.SlackMessengerProvider):
    pass


class LoggerService(sip.LoggerProvider):
    pass
