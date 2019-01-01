from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

from pyspark.sql import SparkSession
from pyspark.sql.functions import window
from pyspark.sql.types import (StructType, StructField,
                               StringType, TimestampType)

spark = SparkSession \
    .builder \
    .appName("StreamingWordTimestamp") \
    .getOrCreate()

schema = StructType([StructField('word', StringType()),
                     StructField('timestamp', TimestampType())])
words = spark.readStream.csv('./word-timestamp-streaming-data', schema)

# Without watermark
# windowedCounts = words.groupBy(
#     window(words.timestamp, "3 minutes", "3 minutes"),
#     words.word
# ).count()

# With watermark
windowedCounts = words.withWatermark("timestamp", "3 minutes").groupBy(
    window(words.timestamp, "3 minutes", "3 minutes"),
    words.word
).count().sort(['window', 'word', 'count'])

# Write counts to console
query = (windowedCounts
         .writeStream
         .outputMode("complete")
         .format("console")
         .start())
