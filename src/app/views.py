from flask import request
from flask.views import MethodView

from src.infrastructure.controllers import APIController


class APIView(MethodView):

    def post(self) -> None:
        request_data = request.json  # Type of the data is dictionary.
        api_controller = APIController()
        api_controller.process_event(request_data)
