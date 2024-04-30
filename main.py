from fastapi import FastAPI
from database.redis import *
from database.mongo import *
from api.mongo import api_mongo
from api.redis import api_redis
import uvicorn

app = FastAPI()

app.include_router(api_mongo,prefix="/mongo",tags=["mongo"])
app.include_router(api_redis,prefix="/redis",tags=["redis"])


@app.on_event("startup")
async def startup_event():
    await connect_to_redis()
    await connect_to_mongo()






if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080,reload=True)
