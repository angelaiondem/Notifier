import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import slack

from src import config
from src.core.entities import EventEntity
from src.core.exceptions import EmailIsNotSentException, \
    SlackMessageIsNotSentException


class SlackService:

    def __init__(
            self,
            slack_token: str,
    ):
        self.__client = slack. WebClient(token=slack_token)

    def send_message(self, event_entity: EventEntity) -> None:
        """
        Post a given message/body to a given slack channel.
        :event_entity body:
        :return None:
        """
        body = dict(event_entity.body)
        try:
            self.__client.chat_postMessage(
                channel=body.get(config.BODY_CHANNEL),
                text=body.get(config.BODY_MESSAGE)
            )
        except Exception as err:
            raise SlackMessageIsNotSentException(err) from None


class EmailService:

    def __init__(
            self,
            smtp_host: str,
            smtp_port: str,
            email_username: str,
            email_app_pass: str,
            from_email: str,
            email_subject: str
    ):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.email_username = email_username
        self.email_app_pass = email_app_pass
        self.from_email = from_email
        self.email_subject = email_subject

    def send_email(self, event_entity: EventEntity) -> None:
        msg = MIMEMultipart()
        msg["From"] = self.from_email
        msg["To"] = event_entity.to
        msg["Subject"] = self.email_subject
        msg.attach(MIMEText(event_entity.body, "plain"))

        try:
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
                smtp.starttls()
                smtp.login(self.email_username, self.email_app_pass)
                msg_text = msg.as_string()
                smtp.sendmail(
                    self.from_email,
                    event_entity.to, msg_text
                )
        except Exception as err:
            raise EmailIsNotSentException(err) from None


class LoggerService:

    def __init__(self,
                 logger_name: str,
                 formatter: str,
                 log_file_path: str,
                 log_level: int
                 ):
        self.logger_name = logger_name
        self.log_format = formatter
        self.log_file_path = log_file_path
        self.log_level = log_level
