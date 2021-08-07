import datetime
import json
import urllib


def _request_data_iss():
    req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
    response = urllib.request.urlopen(req)

    return json.loads(response.read())


class ISSTracking:
    def __init__(self):
        obj = _request_data_iss()
        self.timestamp = obj['timestamp']
        self.location = (obj['iss_position']['latitude'], obj['iss_position']['longitude'])

        '''
        Since the requested time is used to invalidate our cache
        we need to account for timestamp time not aligning with local time since
        we are only supposed to request every 5 seconds max.
        '''
        self.request_time = datetime.datetime.utcnow()

    def get_location(self):
        current_time = datetime.datetime.utcnow()
        if (current_time - self.request_time).total_seconds() > 5:
            obj = _request_data_iss()
            self.timestamp = obj['timestamp']
            self.location = (obj['iss_position']['latitude'], obj['iss_position']['longitude'])
            self.request_time = current_time
        return self.timestamp, self.location

