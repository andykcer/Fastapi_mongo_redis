from fastapi import  APIRouter, HTTPException

from database.redis import *

api_redis = APIRouter()
@api_redis.post("/set/")
async def set_redis_key(key: str, value: str):
    await set_key(key, value)
    return {"message": f"Key '{key}' set to '{value}'"}

@api_redis.get("/get/")
async def get_redis_key(key: str):
    value = await get_key(key)
    if value is None:
        raise HTTPException(status_code=404, detail=f"Key '{key}' not found")
    return {"key": key, "value": value}

@api_redis.delete("/delete/")
async def delete_redis_key(key: str):
    await delete_key(key)
    return {"message": f"Key '{key}' deleted"}
