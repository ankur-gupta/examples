FROM ubuntu:bionic

ENV NAME="neo"

ENTRYPOINT ["/bin/bash", "-c", "echo Hello, ${NAME}"]


# $ docker build . -t entrypoint-example
# $ docker run entrypoint-example
# Hello, neo
# (exits)
# $ docker run -it entrypoint-example /bin/bash
# Hello, neo
# (still exits; no interactive bash shell)
