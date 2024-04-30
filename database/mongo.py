import motor.motor_asyncio
import asyncio
from settings import MONGODB_SETTINGS
# 全局变量，用于存储数据库连接
client = None


async def connect_to_mongo():
    global client
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_SETTINGS['host'], MONGODB_SETTINGS['port'])
        print("Connected to MongoDB successfully!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

# 添加数据
async def add_data(collection, data):
    try:
        db = client['test_db']
        collection = db[collection]
        await collection.insert_one(data)
        print("Data added successfully!")
    except Exception as e:
        print(f"Error adding data: {e}")

# 批量添加数据
async def bulk_insert_data(collection, data_list):
    try:
        db = client['test_db']
        collection = db[collection]
        result = await collection.insert_many(data_list)
        print(f"{len(result.inserted_ids)} documents inserted successfully!")
    except Exception as e:
        print(f"Error bulk inserting data: {e}")


# 删除数据
async def delete_data(collection, query):
    try:
        db = client['test_db']
        collection = db[collection]
        await collection.delete_one(query)
        print("Data deleted successfully!")
    except Exception as e:
        print(f"Error deleting data: {e}")

# 修改数据
async def update_data(collection, query, update_data):
    try:
        db = client['test_db']
        collection = db[collection]
        await collection.update_one(query, update_data)
        print("Data updated successfully!")
    except Exception as e:
        print(f"Error updating data: {e}")

# 查询数据
async def find_data(collection, query):
    try:
        db = client['test_db']
        collection = db[collection]
        result = await collection.find_one(query)
        print("Data found successfully!")
        print(result)
    except Exception as e:
        print(f"Error finding data: {e}")

# 聚合查询数据
async def aggregate_data(collection, pipeline):
    try:
        db = client['test_db']
        collection = db[collection]
        result = await collection.aggregate(pipeline).to_list(length=None)
        print("Data aggregated successfully!")
        print(result)
    except Exception as e:
        print(f"Error aggregating data: {e}")

