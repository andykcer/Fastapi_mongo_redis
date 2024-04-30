import asyncio
import aioredis
from aioredis import Redis
from settings import REDIS_SETTINGS

redis_client: Redis | None = None

async def connect_to_redis():
    print("Connecting to redis...")
    global redis_client
    redis_client = await aioredis.from_url(
        url=REDIS_SETTINGS['url'],
        port=REDIS_SETTINGS['port'],
        password=REDIS_SETTINGS['password'],
        db=REDIS_SETTINGS['db'],
        encoding=REDIS_SETTINGS['encoding'],
        decode_responses=REDIS_SETTINGS['decode_responses'],
    )
    try:
        pong = await redis_client.ping()
        #print(pong)
        print("Connected to redis")
    except Exception as e:
        print(f"Failed to connect to redis: {e}")
        redis_client = None

async def set_key(key: str, value: str):
    if not redis_client:
        print("Not connected to Redis.")
        return
    await redis_client.set(key, value)
    print(f"Set key '{key}' to '{value}'")

async def get_key(key: str):
    if not redis_client:
        print("Not connected to Redis.")
        return
    value = await redis_client.get(key)
    print(f"Value of key '{key}': {value}")
    return value

async def delete_key(key: str):
    if not redis_client:
        print("Not connected to Redis.")
        return
    await redis_client.delete(key)
    print(f"Deleted key '{key}'")

