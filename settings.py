#连接redis数据库
REDIS_SETTINGS={
        'url':'redis://localhost',
        'port':'6379',
        'password':'123456',
        'db':'1',
        'encoding':"utf-8",
        "decode_responses":True,
}


# 连接Mongo数据库
MONGODB_SETTINGS = {
    'host': 'localhost',
    'port': 27017,
    'db_name': 'test_db'
}