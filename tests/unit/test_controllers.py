import json
import unittest
from os.path import join, dirname, abspath

from flask import Flask

from src.infrastructure.controllers import APIController


class TestAPIController(unittest.TestCase):

    def setUp(self) -> None:
        self.app = Flask(__name__)
        self.api_controller = APIController()

    def test_controller_new_publication(self) -> None:
        expected_result = [200, 400, 400, 400]
        actual_list = []
        file_path_new_publication = join(dirname(dirname(abspath(__file__))),
                                         "events", "new_publication.json")
        with open(file_path_new_publication) as file:
            json_file_data = json.load(file)
            for i in json_file_data:
                with self.app.app_context():
                    response = self.api_controller.process_event(i)
                    actual_list.append(response[1])
            self.assertTrue(actual_list == expected_result)

    def test_controller_approved_publication(self) -> None:
        expected_result = [200, 400, 400, 400, 400]
        actual_list = []
        file_path_new_publication = join(dirname(dirname(abspath(__file__))),
                                         "events", "approved_publication.json")
        with open(file_path_new_publication) as file:
            json_file_data = json.load(file)
            for i in json_file_data:
                with self.app.app_context():
                    response = self.api_controller.process_event(i)
                    actual_list.append(response[1])
            self.assertTrue(actual_list == expected_result)
