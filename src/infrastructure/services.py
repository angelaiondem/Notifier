import smtplib

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
        send_errs = s.sendmail(self.from_email, to_email, msg_text)
        print(send_errs)
        s.quit()


class SlackService:
    pass


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
