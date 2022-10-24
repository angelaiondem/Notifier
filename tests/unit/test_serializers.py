import unittest
import logging
from os.path import join, dirname, abspath

from src import config
from src.core.exceptions import InvalidEventTypeException, \
    MessageBodyIsInvalidException, InvalidEmailException
from src.infrastructure.providers import LoggerServiceProvider
from src.infrastructure.serializers import EventSerializer
from src.core.entities import EventEntity
from src.infrastructure.services import LoggerService


class TestSerializers(unittest.TestCase):

    def setUp(self) -> None:
        self.log_file_path = join((dirname(abspath(__file__))), "notifier.log")
        logger_service_provider = LoggerServiceProvider(LoggerService(
            logger_name=logging.getLogger(__name__).name,
            formatter=config.DEFAULT_LOG_FORMAT,
            log_file_path=self.log_file_path,
            log_level=config.DEFAULT_LOG_LEVEL))
        self.serializer = EventSerializer(logger_service_provider)

    def test_serialize(self):
        self.assertEqual(self.serializer.serialize(
            EventEntity(
                event_type="new_publication",
                body="Hi.",
                to=None)
        ),
            {"event_type": "new_publication",
             "body": "Hi.",
             "to": None})

        self.assertEqual(self.serializer.serialize(
            EventEntity(
                event_type="approved_publication",
                body="This is a Test message.",
                to="ang@gmail.com")
        ),
            {"event_type": "approved_publication",
             "body": "This is a Test message.",
             "to": "ang@gmail.com"})

        self.assertEqual(self.serializer.serialize(
            EventEntity(
                event_type="new_publication",
                body="Hello.",
                to="davit@gmail")
        ),
            {"event_type": "new_publication",
             "body": "Hello.",
             "to": "davit@gmail"})

    def test_serializer_InvalidEventTypeException(self):
        self.assertRaises(InvalidEventTypeException,
                          self.serializer.serialize,
                          EventEntity(event_type="_publication",
                                      body="Hi.", to="angela@yahoo.com"))

    def test_serializer_MessageBodyIsInvalidException(self):
        self.assertRaises(MessageBodyIsInvalidException,
                          self.serializer.serialize,
                          EventEntity(event_type="new_publication",
                                      body="", to="angela@gmail.com"))

    def test_serializer_InvalidEmailException(self):
        self.assertRaises(InvalidEmailException, self.serializer.serialize,
                          EventEntity(event_type="approved_publication",
                                      body="Hi.", to=None))

    def test_serializer_Exception(self):
        self.assertRaises(Exception, self.serializer.serialize,
                          EventEntity(event_type="approved_publication",
                                      body={"msg": "Hi."}, to="a@yahoo.com"))

    def test_deserialize(self):
        self.assertEqual(self.serializer.deserialize(
            {"event_type": "new_publication",
             "body": "Hi.",
             "to": None}
        ),
            EventEntity(
                event_type="new_publication",
                body="Hi.",
                to=None)
        )
        self.assertEqual(self.serializer.deserialize(
            {"event_type": "approved_publication",
             "body": "Test message.",
             "to": "anzhela.iondem@gmail.com"}
        ),
            EventEntity(
                event_type="approved_publication",
                body="Test message.",
                to="anzhela.iondem@gmail.com")
        )
        self.assertEqual(self.serializer.deserialize(
            {"event_type": "new_publication",
             "body": "Hi.",
             "to": "anzhela@gmail"}
        ),
            EventEntity(
                event_type="new_publication",
                body="Hi.",
                to="anzhela@gmail"
            )
        )

    def test_deserializer_InvalidEventTypeException(self):
        self.assertRaises(InvalidEventTypeException,
                          self.serializer.deserialize,
                          {"event_type": "_publication",
                           "body": "Hi.", "to": "angela@gmail.com"})

    def test_deserializer_MessageBodyIsInvalidException(self):
        self.assertRaises(MessageBodyIsInvalidException,
                          self.serializer.deserialize,
                          {"event_type": "new_publication",
                           "body": "", "to": "anna@yahoo.com"})

    def test_deserializer_InvalidEmailException(self):
        self.assertRaises(InvalidEmailException, self.serializer.deserialize,
                          {"event_type": "approved_publication",
                           "body": "Hi.", "to": None})

    def test_deserializer_Exception(self):
        self.assertRaises(Exception, self.serializer.deserialize,
                          {"event_type": "approved_publication",
                           "body": {"msg": "Hi."}, "to": "a@yahoo.com"})
