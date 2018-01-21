"""
Subscriber
"""
import logging
import os

import redis

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
logging.basicConfig()


class Sub(object):
    """A simple class that subscribes to a 
    Redis pub/sub channel and echoes whatever
    it gets
    """

    def __init__(self, rconn, channel_name):
        """Create a Sub object

        Args:
            channel_name (str): Name of the channel to listen on

        Returns:
            A Sub object
        """
        self.redis = rconn
        self.channel = channel_name
        self.sub = self.redis.pubsub(ignore_subscribe_messages=True)
        self.sub.subscribe(channel_name)

    def run(self):
        """Subscribe to channel and echo
        """
        LOGGER.info('Starting to listen...')
        for msg in self.sub.listen():
            LOGGER.info('Sub received: %s', msg['data'])


if __name__ == "__main__":
    redis_host = os.getenv('REDIS', 'localhost')
    channel = os.getenv('SCHANNEL', 'default_sub_channel')
    rconn = redis.StrictRedis(host=redis_host)
    sub = Sub(rconn, channel)
    sub.run()