import unittest

import src.infrastructure.serializers as sis
from src.core.entities import EventEntity


class TestSerializers(unittest.TestCase):

    def test_serialize(self):
        self.assertEqual(sis.EventSerializer.serialize(
            EventEntity(
                event_type="new_publication",
                body={"channel": "", "message": ""},
                to="ani@gmail.com")
        ),
            {"event_type": "new_publication",
             "body": {"channel": "", "message": ""},
             "to": "ani@gmail.com"}
        )
        self.assertEqual(sis.EventSerializer.serialize(
            EventEntity(
                event_type="approved_publication",
                body="This is a Test message.",
                to="ang@gmail.com")
        ),
            {"event_type": "approved_publication",
             "body": "This is a Test message.",
             "to": "ang@gmail.com"}
        )
        self.assertEqual(sis.EventSerializer.serialize(
            EventEntity(
                event_type="new_publication",
                body={"channel": "", "message": ""},
                to="davit@gmail")
        ),

            {"event_type": "new_publication",
             "body": {"channel": "", "message": ""},
             "to": "davit@gmail"}
        )
        with self.assertRaises(Exception):
            sis.EventSerializer.serialize(
                EventEntity(
                    event_type="_publication",
                    body={"channel": "", "message": ""},
                    to="angela@gmail.com")
            )
        with self.assertRaises(Exception):
            sis.EventSerializer.serialize(
                EventEntity(
                    event_type="new_publication",
                    body={"channel": "", "msg": ""},
                    to="anna@yahoo.com"
                )
            )
        with self.assertRaises(Exception):
            sis.EventSerializer.serialize(
                EventEntity(
                    event_type="approved_publication",
                    body={"channel": "", "message": ""},
                    to="anzhela.iondem@gmail")
            )

    def test_deserialize(self):
        self.assertEqual(sis.EventSerializer.deserialize(
            {"event_type": "new_publication",
             "body": {"channel": "", "message": ""},
             "to": "angelaiondem@gmail.com"}
        ),
            EventEntity(
                event_type="new_publication",
                body={"channel": "", "message": ""},
                to="angelaiondem@gmail.com")
        )
        self.assertEqual(sis.EventSerializer.deserialize(
            {"event_type": "approved_publication",
             "body": "Test message.",
             "to": "anzhela.iondem@gmail.com"}
        ),
            EventEntity(
                event_type="approved_publication",
                body="Test message.",
                to="anzhela.iondem@gmail.com")
        )
        self.assertEqual(sis.EventSerializer.deserialize(
            {"event_type": "new_publication",
             "body": {"channel": "", "message": ""},
             "to": "anzhela@gmail"}
        ),
            EventEntity(
                event_type="new_publication",
                body={"channel": "", "message": ""},
                to="anzhela@gmail"
            )
        )
        with self.assertRaises(Exception):
            sis.EventSerializer.deserialize(
                {"event_type": "_publication",
                 "body": {"channel": "", "message": ""},
                 "to": "angela@gmail.com"})
        with self.assertRaises(Exception):
            sis.EventSerializer.deserialize(
                {"event_type": "new_publication",
                 "body": {"channel": "", "msg": ""},
                 "to": "anna@yahoo.com"}
            )
        with self.assertRaises(Exception):
            sis.EventSerializer.deserialize(
                {"event_type": "approved_publication",
                 "body": {"channel": "", "message": ""},
                 "to": "anzhela.iondem@gmail"}
            )
