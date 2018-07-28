from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

import folium

# Make a map
m = folium.Map(location=[45.5236, -122.6750])
m.save('index.html')


# Links:
# https://python-visualization.github.io/folium/quickstart.html
