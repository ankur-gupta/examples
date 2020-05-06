FROM jupyter/pyspark-notebook

USER root

# RUN apt-get install -y openssh
RUN sed -i 's/^# deb-src/deb-src/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y iputils-ping openssh-server openssh-client

# This is needed to start spark
RUN mkdir -p /usr/local/spark/logs
RUN chown $NB_UID /usr/local/spark/logs

RUN mkdir -p /usr/local/spark/work
RUN chown $NB_UID /usr/local/spark/work
USER $NB_UID


# Build/run:
# docker build . -t pyspark-notebook-modified
# docker run -it pyspark-notebook-modified /bin/bash
