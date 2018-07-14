import json
from datetime import datetime
from pytz import timezone

TYPE = '__type__'
DATETIME = 'datetime'


class DateTimeEncoder(json.JSONEncoder):
    def default(self, python_object):
        if isinstance(python_object, datetime):
            json_object = {
                TYPE: DATETIME,
                'year': python_object.year,
                'month': python_object.month,
                'day': python_object.day,
                'hour': python_object.hour,
                'minute': python_object.minute,
                'second': python_object.second,
                'microsecond': python_object.microsecond,
                'tzinfo': None
            }
            if python_object.tzinfo is not None:
                json_object['tzinfo'] = str(python_object.tzinfo)
        else:
            json_object = json.JSONEncoder.default(self, python_object)
        return json_object


class DateTimeDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.json_to_python,
                         *args, **kwargs)

    def json_to_python(self, json_object):
        if (TYPE in json_object and
                json_object[TYPE] == DATETIME and
                'tzinfo' in json_object):

            # Save two fields before we attempt to parse the date
            object_type = json_object.pop(TYPE)
            object_tzinfo = json_object['tzinfo']
            if json_object['tzinfo'] is not None:
                json_object['tzinfo'] = timezone(json_object['tzinfo'])
            try:
                python_object = datetime(**json_object)
                return python_object
            except:
                # We failed to parse the date. Re-create original json_object
                # and return in.
                json_object[TYPE] = object_type
                json_object['tzinfo'] = object_tzinfo
                return json_object
        else:
            return json_object
