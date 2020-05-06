# Docker Compose Tutorial

Based on the official
[Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/).

## Steps
1. Install docker from  [Docker Desktop for Mac - Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-mac/).
You may need to enter your password because Docker does need privileged access.
There should be no need to sign up for a Docker Hub account.
Ensure that Docker is running on your machine.
You should be able to find `docker` and `docker-compose` executables in your
PATH on the command line. Type these in a terminal to check:
    ```bash
    which docker
    # /usr/local/bin/docker

    type docker
    # docker is /usr/local/bin/docker

    which docker-compose
    # /usr/local/bin/docker-compose

    type docker-compose
    # docker-compose is /usr/local/bin/docker-compose
    ```

2. Follow the instructions in
[Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/).
You should see the two containers running:

    ```bash
    > docker image ls
    REPOSITORY                    TAG                 IMAGE ID            CREATED             SIZE
    docker-compose-tutorial_web   latest              c52e96d856c5        56 seconds ago      220MB
    redis                         alpine              360360313017        19 hours ago        31.6MB
    python                        3.7-alpine          61681f520204        3 days ago          96MB
    ```

    ```bash
    > docker ps
    CONTAINER ID        IMAGE                         COMMAND                  CREATED              STATUS              PORTS                    NAMES
    9c406a2a9e2c        docker-compose-tutorial_web   "flask run"              About a minute ago   Up About a minute   0.0.0.0:5000->5000/tcp   docker-compose-tutorial_web_1
    ecfd88a92334        redis:alpine                  "docker-entrypoint.s…"   About a minute ago   Up About a minute   6379/tcp                 docker-compose-tutorial_redis_1
    ```

3. If you stop the application (either by pressing `Control+C` or by running
`docker-compose down`), you should see the running containers disappear
when you run `docker ps`.

4. You can also use `docker-compose ps` to see the containers specific to
docker compose _in that folder only_. For example, this is what you can expect to see when the
docker compose is running.
    ```bash
    > docker-compose ps
                 Name                            Command               State           Ports
    -------------------------------------------------------------------------------------------------
    docker-compose-tutorial_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
    docker-compose-tutorial_web_1     flask run                        Up      0.0.0.0:5000->5000/tcp
    ```
   Once you stop docker compose, you should see empty output for
   `docker-compose ps`.
