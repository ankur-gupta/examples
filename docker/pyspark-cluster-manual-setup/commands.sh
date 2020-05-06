#!/usr/bin/env bash

docker network create --driver bridge manual-net
docker network ls
#NETWORK ID          NAME                              DRIVER              SCOPE
#5c7d8e89267c        manual-net                        bridge              local
docker network inspect manual-net
# Json file output
docker run -dit --name manual-spark-master --network manual-net pyspark-notebook-modified /bin/bash
docker run -dit --name manual-spark-worker-1 --network manual-net pyspark-notebook-modified /bin/bash
docker container ls
#CONTAINER ID        IMAGE                      COMMAND                  CREATED             STATUS              PORTS                                                      NAMES
#c28de9fe2986        pyspark-notebook-modified   "tini -g -- /bin/bash"   6 seconds ago       Up 6 seconds        8888/tcp                                                   manual-spark-worker-1
#e2826c0a044e        pyspark-notebook-modified   "tini -g -- /bin/bash"   17 seconds ago      Up 17 seconds       8888/tcp                                                   manual-spark-master


# Inspect again
docker network inspect manual-net
# Should contain manual-spark-master and manual-spark-worker-1

# Manually, ping the worker
docker container attach manual-spark-master
# Inside docker. These worked for me last time. No packet loss.
ping -c 2 google.com
ping -c 2 manual-spark-worker-1
# Escape sequence without killing the container:

export SPARK_MASTER_HOST=manual-spark-master
echo $SPARK_MASTER_HOST
/usr/local/spark/sbin/start-master.sh

# No need to set ports because defaults are okay.
# Hold down Control, press p and the q.


docker container attach manual-spark-worker-1
# Inside docker container:
ping -c 2 google.com
ping -c 2 manual-spark-master
/usr/local/spark/sbin/start-slave.sh spark://manual-spark-master:7077
# No need to set ports because defaults are okay.
# Hold down Control, press p and the q.

docker container attach manual-spark-master
# Inside docker:
/usr/local/spark/bin/spark-shell --master spark://manual-spark-master:7077
python
# Within python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('my_app').master('spark://manual-spark-master:7077').getOrCreate()
# You can see the app created in the worker!
# Hold down Control, press p and the q.

# Cleanup
docker container stop manual-spark-master manual-spark-worker-1
docker container rm manual-spark-master manual-spark-worker-1
docker network rm manual-net
