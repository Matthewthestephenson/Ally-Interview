import json
import urllib
from datetime import datetime
from collections import defaultdict


'''
Request the data from the endpoint.
Converts to dictionary craft -> people
'''
def _request_data_ship_dict():
    req = urllib.request.Request("http://api.open-notify.org/astros.json")
    response = urllib.request.urlopen(req)

    obj = json.loads(response.read())

    crafts_people_dict = defaultdict(list)

    for entry in obj['people']:
        crafts_people_dict[entry['craft']].append(entry['name'])

    return dict(crafts_people_dict)


class Crafts:
    def __init__(self):
        self.request_time = datetime.utcnow()
        self.crafts_people_dict = _request_data_ship_dict()

    def get_craft_people(self):
        current_time = datetime.utcnow()
        # lower load on server, this data is manually updated,
        # we can timeout much slower.
        if (current_time - self.request_time).total_seconds() > 10000:
            self.request_time = datetime.utcnow()
            self.crafts_people_dict = _request_data_ship_dict()

        return self.crafts_people_dict
