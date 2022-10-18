from flask import request
from flask.views import MethodView

from src.infrastructure.controllers import APIController


class APIView(MethodView):

    def post(self) -> None:
        """
        Catch the POST requests and send the data to API controller.
        :return None:
        """
        request_data = request.json  # The type of received data is dictionary.
        api_controller = APIController()
        api_controller.process_event(request_data)
