import logging
from os.path import join, dirname, abspath

# Logging configurations.
LOGGER_NAME = logging.getLogger(__name__)
LOG_FILE_PATH = join(dirname(dirname(abspath(__file__))), "notifier.log")
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(asctime)s: %(levelname)s: %(name)s: %(message)s"

# Email service configuration
SMTP_HOST = "SMTP_HOST"
SMTP_PORT = "SMTP_PORT"
EMAIL_USERNAME = "EMAIL_USERNAME"
EMAIL_APP_PASS = "EMAIL_APP_PASS"
FROM_EMAIL = "FROM_EMAIL"
