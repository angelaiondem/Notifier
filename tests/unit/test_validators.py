import unittest

import src.core.validators as scv


class TestValidators(unittest.TestCase):

    def test_check_email_validation(self):
        self.assertTrue(scv.check_email_validation("anzhela.iondem@gmail.com"))
        self.assertTrue(scv.check_email_validation("angela@yahoo.com"))
        self.assertRaises(Exception, scv.check_email_validation, "angela@gmail")
        self.assertRaises(Exception, scv.check_email_validation, "angela")

    def test_check_event_type(self):
        self.assertTrue(scv.check_event_type("approved_publication"))
        self.assertTrue(scv.check_event_type("new_publication"))
        self.assertRaises(Exception, scv.check_event_type, "_publication")
        self.assertRaises(Exception, scv.check_event_type, "")

    def test_check_to_be_dict(self):
        self.assertTrue(scv.check_to_be_dict({'a': 'a', 'b': 'b'}))
        self.assertRaises(Exception, scv.check_to_be_dict, "'a': 'a', 'b': 'b'")

    def test_check_body_dict_content(self):
        self.assertTrue(scv.check_body_dict_keys(
            {"channel": "", "message": ""})
        )
        with self.assertRaises(Exception):
            scv.check_body_dict_keys({"channel": "", "msg": ""})
