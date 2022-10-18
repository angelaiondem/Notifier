import logging
from os.path import join, dirname, abspath

# Logging configurations.
LOGGER_NAME = logging.getLogger(__name__)
LOG_FILE_PATH = join(dirname(dirname(abspath(__file__))), "notifier.log")
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(asctime)s: %(levelname)s: %(message)s"


# Email service configuration .
SMTP_HOST = "SMTP_HOST"  # From .env file
SMTP_PORT = "SMTP_PORT"  # From .env file
EMAIL_USERNAME = "EMAIL_USERNAME"  # From .env file
EMAIL_APP_PASS = "EMAIL_APP_PASS"  # From .env file
FROM_EMAIL = "FROM_EMAIL"  # From .env file
EMAIL_SUBJECT = "Approved publication"


# Slack configurations.
SLACK_CHANNEL = "#notifier_new_publication"
SLACK_TOKEN = "SLACK_TOKEN"  # From .env file


# Event Types.
NEW_PUBLICATION = "new_publication"
APPROVED_PUBLICATION = "approved_publication"
