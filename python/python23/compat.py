# StringIO
# Used for reading dataframe from a string
# df = pd.DataFrame(StringIO(string))
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

# datetime
# Doesn't need a compat file.

