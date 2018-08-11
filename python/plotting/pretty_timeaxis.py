from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Beautify dates on the xaxis but don't modify the ticks.
# Jupyter has its own date formatter. These effects below may only
# be needed for ipython.

# This line may not be needed.
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Y %Z'))

# This line works almost every time.
plt.gcf().autofmt_xdate()


# Sometimes, we need to modify the ticks as well. The following code
# modifies both major ticks and major tick labels.
days = mdates.DayLocator()
hours = mdates.HourLocator()
dfmt = mdates.DateFormatter('%b %d')
plt.gca().xaxis.set_major_locator(days)
plt.gca().xaxis.set_major_formatter(dfmt)
plt.gcf().autofmt_xdate()
