from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Beautify dates on the xaxis
# Jupyter has its own date formatter. These effects below may only
# be needed for ipython.

# This line may not be needed.
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Y %Z'))

# This line works almost every time.
plt.gcf().autofmt_xdate()
