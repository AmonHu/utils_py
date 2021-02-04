from redis import Redis
import json


class RedisClient(object):
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db

    def get(self, key):
        with Redis(host=self.host, port=self.port, db=self.db) as redis:
            return json.loads(redis.get(key))

    def set(self, key, value):
        with Redis(host=self.host, port=self.port, db=self.db) as redis:
            return redis.set(key, json.dumps(value.__dict__, ensure_ascii=False))

    @property
    def keys(self):
        with Redis(host=self.host, port=self.port, db=self.db) as redis:
            return redis.keys()
