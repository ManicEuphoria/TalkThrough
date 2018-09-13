# coding: utf-8
import os


PROJECT_CONFIG = {
    "host": "127.0.0.1",
    "port": "8888",
    "debug": True
}

MONGO_CONFIG = {
    "host": "127.0.0.1",
    "port": 27017,
}

SQL_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "username": "",
    "password": ""
}

REDIS_CONFIG = {
    "host": "",
    "port": 0
}


DIR_PATH = os.path.dirname(__file__)
PATH = os.path.dirname(DIR_PATH)
