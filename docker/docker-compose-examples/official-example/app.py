import time
import redis
from flask import Flask

app = Flask(__name__)

# 'redis' is the hostname of the redis container and we use the default port
# for redis which is 6379.
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as e:
            # If redis service is not available, we try for again a few times
            # and then fail. This is useful when the application comes online
            # but also makes our service more resilient, especially if we
            # restart redis service.
            if retries == 0:
                raise e
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    return f"Hello World from Docker! I have been seen {get_hit_count()} times"
