from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

from datetime import datetime, timedelta
from pytz import timezone, UTC

x = datetime(2018, 9, 23, 0, 0, 0, tzinfo=UTC)
y = x - timedelta(minutes=23)
print(x)
print(y)

# Another way to generate timezones:
utc = timezone('UTC')
assert utc == UTC

la = timezone('America/Los_Angeles')
pt = timezone('US/Pacific')


def utcnow():
    # Return a timezone aware object.
    # datetime.utcnow() is the correct UTC time but it's not timezone
    # aware.
    return datetime.utcnow().replace(tzinfo=UTC)


# Recommendation is to work with timezone aware objects only as long as
# possible.
# Exception: pandas columns may have to be made timezone naive
# for better type inference.

current_time_in_utc = utcnow()
current_time_supposedly_in_pt = current_time_in_utc.replace(tzinfo=pt)
print(current_time_in_utc)
print(current_time_supposedly_in_pt)

# This prints ~7:53 which means that simply replacing the tzinfo
# is not correct way to transform the timezone.
print(current_time_supposedly_in_pt - current_time_in_utc)

# Correct way is this:
current_time_in_pt = current_time_in_utc.astimezone(pt)
print(current_time_in_utc)
print(current_time_in_pt)

# This prints 0:0 which is the correct answer.
print(current_time_in_pt - current_time_in_utc)
