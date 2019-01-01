from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

import os
import time
import pandas as pd
import numpy as np
import tempfile
from datetime import datetime, timedelta
from pytz import timezone, UTC
from csv import QUOTE_ALL


WORDS = ['apache', 'spark', 'hadoop', 'python', 'java', 'scala']
# FORMAT = '.json'
FORMAT = '.csv'

for _ in range(1000):
    words = np.random.choice(WORDS, size=5, replace=True)
    # timestamp = datetime.utcnow().replace(tzinfo=UTC)
    timestamp = datetime.utcnow() - timedelta(minutes=np.random.randint(0, 6))
    data = pd.DataFrame({'word': words})
    data['timestamp'] = timestamp
    data['timestamp'] = data['timestamp'].apply(lambda x: x.isoformat())
    # data['timestamp'] = pd.to_datetime(data['timestamp'])
    path_to_file = tempfile.mkstemp(
        FORMAT,
        'word-timestamp-',
        dir='./word-timestamp-streaming-data')[1]
    try:
        if FORMAT == '.csv':
            data.to_csv(path_to_file, index=False, quoting=QUOTE_ALL)
        elif FORMAT == '.json':
            data.to_json(path_to_file)
        else:
            if os.path.exists(path_to_file):
                os.remove(path_to_file)
    except KeyboardInterrupt as e:
        if os.path.exists(path_to_file):
            os.remove(path_to_file)
        raise e
    print(path_to_file)
    time.sleep(3)
