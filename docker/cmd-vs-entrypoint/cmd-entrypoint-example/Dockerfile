FROM ubuntu:bionic

ENV NAME="neo"
ENTRYPOINT ["/bin/bash", "-c", "echo Hello, ${NAME}"]
CMD ["/bin/bash", "-c", "echo Hello, ${NAME}"]


# $ docker build . -t cmd-entrypoint-example
# $ docker run cmd-entrypoint-example
# Hello, neo
# (exits)
# $ docker run -it cmd-entrypoint-example /bin/bash
# Hello, neo
# (still exits; no interactive bash shell)
