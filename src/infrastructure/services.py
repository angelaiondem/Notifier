import smtplib
import slack
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailService:

    def __init__(
            self,
            smtp_host: str,
            smtp_port: str,
            email_username: str,
            email_app_pass: str,
            from_email: str
    ):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.email_username = email_username
        self.email_app_pass = email_app_pass
        self.from_email = from_email

    def send_email(self, email_subject, to_email, email_body):
        msg = MIMEMultipart()
        msg["From"] = self.from_email
        msg["To"] = to_email
        msg["Subject"] = email_subject
        msg.attach(MIMEText(email_body, "plain"))

        s = smtplib.SMTP(self.smtp_host, self.smtp_port)
        s.starttls()
        s.login(self.email_username, self.email_app_pass)
        msg_text = msg.as_string()
        s.sendmail(from_addr=self.from_email, to_addrs=to_email, msg=msg_text)
        s.quit()


class SlackService:

    def __init__(self, slack_token: str):
        self.__slack_token = slack_token
        self.__client = slack.WebClient(token=self.__slack_token)

    def send_message(self, channel: str, body: str):
        self.__client.chat_postMessage(channel=channel, text=body)


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
