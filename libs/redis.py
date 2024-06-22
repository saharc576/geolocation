"""Redis client for the Redis database"""
import redis
import json
from typing import Optional, Union

# default parameters for redis client
_DEFAULT_HOST = "redis"
_DEFAULT_PORT = 6379
_DEFAULT_DB = 0
_DEFAULT_EXPIRATION = 60 * 60  # 1 hour default expiration (in seconds)

class RedisClient:
    def __init__(self, host: str = _DEFAULT_HOST, port: int = _DEFAULT_PORT, db: int = _DEFAULT_DB):
        """
        Initialize the Redis client.

        :param host: The hostname of where the server is running 
            In our case, the docker-compose name.
        """
        self.client = redis.Redis(host=host, port=port, db=db)

    def set_value(self, key: str, value: Union[str, dict, list], expiration_seconds: int = _DEFAULT_EXPIRATION):
        """
        Set a JSON-serializable value in Redis under the specified key.
        The value is set with a timeout.

        :param expiration_seconds: The time item will exist in the db.
        """
        self.client.setex(name=key, value=json.dumps(value), time=expiration_seconds)

    def get_value(self, key: str) -> Optional[Union[str, dict, list, None]]:
        """
        Retrieve and deserialize a value from Redis.
        If value was not found, return None.
        """
        value = self.client.get(key)
        if value is None:
            return None
        return json.loads(value)
