from fastapi import  APIRouter, HTTPException

from database.mongo import *

api_mongo = APIRouter()


# 添加数据
@api_mongo.post("/add/")
async def add_mongo_data(collection: str, data: dict):
    await add_data(collection, data)
    return {"message": "Data added successfully!"}

# 删除数据
@api_mongo.delete("/delete/")
async def delete_mongo_data(collection: str, query: dict):
    await delete_data(collection, query)
    return {"message": "Data deleted successfully!"}

# 修改数据
@api_mongo.put("/update/")
async def update_mongo_data(collection: str, query: dict, update_data: dict):
    await update_data(collection, query, update_data)
    return {"message": "Data updated successfully!"}

# 查询数据
@api_mongo.get("/find/")
async def find_mongo_data(collection: str, query: dict):
    result = await find_data(collection, query)
    if not result:
        raise HTTPException(status_code=404, detail="Data not found")
    return result

# 聚合查询数据
@api_mongo.get("/aggregate/")
async def aggregate_mongo_data(collection: str, pipeline: list):
    result = await aggregate_data(collection, pipeline)
    return result