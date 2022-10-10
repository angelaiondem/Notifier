import json

import requests
from flask import Flask, request
from flask.views import MethodView

from src.infrastructure.controllers import APIController


class APIView(MethodView):

    def post(self):
        data = request.json
        api_controller = APIController()
        print(data)
        return data


def main():
    app = Flask(__name__)
    app.add_url_rule("/", view_func=APIView.as_view("/"))
    app.run()


if __name__ == "__main__":
    main()
