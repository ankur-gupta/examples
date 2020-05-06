FROM ubuntu:bionic

ENV NAME="neo"

CMD ["/bin/bash", "-c", "echo Hello, ${NAME}"]


# $ docker build . -t cmd-example
# $ docker run cmd-example
# Hello, neo
# (exits)
# $ docker run -it cmd-example /bin/bash
# root@93d6a128cf8c:/#
# (no message printed; just an interactive shell)
