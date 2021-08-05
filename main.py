import urllib.request
import json


def get_iss_data_dict():
    req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
    response = urllib.request.urlopen(req)

    obj = json.loads(response.read())

    print(obj['timestamp'])
    print(obj)


def get_people_space():
    req = urllib.request.Request("http://api.open-notify.org/astros.json")
    response = urllib.request.urlopen(req)

    obj = json.loads(response.read())

    print(obj)


get_iss_data_dict()
get_people_space()
