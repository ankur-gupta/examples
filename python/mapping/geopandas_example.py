from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

from shapely.geometry import Point
import pandas as pd
import geopandas as gpd
from shapely.wkt import loads

# Create a GeoSeries
x = gpd.GeoSeries([loads('POINT(1 2)'),
                   loads('POINT(1.5 2.5)'),
                   loads('POINT(2 3)')])
y = gpd.GeoSeries([Point(-120, 45), Point(-121.2, 46), Point(-122.9, 47.5)])

# Check projections (there should be none; we didn't put any)
x.crs
y.crs

# Let's assign projections.
x.crs = {'init': 'epsg:4326'}
y.crs = {'init': 'epsg:4326'}

# Let's plot these.
x.plot()
y.plot()

# Let's create using another way.
# This is a list of shapely Points
data = {'name': ['a', 'b', 'c'],
        'lat': [45, 46, 47.5],
        'long': [-120, -121.2, -122.9]}
list_of_points = [Point(point) for point in zip(data['long'], data['lat'])]
z = gpd.GeoSeries(list_of_points, index=data['name'])

# Or, use a GeoDataFrame
df = pd.DataFrame(data)
geometry = [Point(xy) for xy in zip(df['long'], df['lat'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Read shapefile
path_to_shapefile = gpd.datasets.get_path('naturalearth_lowres')
world = gpd.read_file(path_to_shapefile)
world.to_json()

# Links
# http://geopandas.org/mergingdata.html
# (weak) https://geohackweek.github.io/vector/04-geopandas-intro/
# (too cumbersome) https://programminghistorian.org/lessons/mapping-with-python-leaflet
