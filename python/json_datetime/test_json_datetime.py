from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

import json
from datetime import datetime
from pytz import UTC
from json_datetime import DateTimeEncoder, DateTimeDecoder


class TestDateTimeEncodingDecoding:

    def test_encoding_decoding_mixed(self):
        python_object = {'name': 'Rick Sanchez',
                         'country': 'USA',
                         'dimension': 'C-137',
                         'family': ['Morty', 'Summer', 'Beth', 'Jerry'],
                         'current_date': datetime.utcnow().replace(tzinfo=UTC)
                         }
        json_string = json.dumps(python_object, cls=DateTimeEncoder)
        assert json.loads(json_string, cls=DateTimeDecoder) == python_object
