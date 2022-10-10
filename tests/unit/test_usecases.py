import json

import requests


def post(data_dict):
    data_json = json.dumps(data_dict)
    respond = requests.post(json=data_json, url="http://127.0.0.1:5000")
    print(respond)


f = {
    "event_type": "new_publication",
    "body": "Organizing what’s happening in the world to help you learn more about the stories that matter. Learn more at news.google.com.",
    "to": "anzhela.iondem@gmail.com"
}
post(f)
