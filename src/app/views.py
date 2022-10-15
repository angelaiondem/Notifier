from flask import request
from flask.views import MethodView

from src.infrastructure.controllers import APIController


class APIView(MethodView):

    @staticmethod
    def post():
        request_data = request.json
        print(type(request_data))

        api_controller = APIController()
        api_controller.process_event(request_data)
        return request_data
