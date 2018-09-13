# coding: utf-8

PROJECT_CONFIG = {
    "host": "",
    "port": "",
    "debug": False
}

MONGO_CONFIG = {
    "host": "",
    "port": 27017,
}

SQL_CONFIG = {
    "host": "",
    "port": 3306,
    "username": "",
    "password": ""
}

REDIS_CONFIG = {
    "host": "",
    "port": 0
}

# project abspath
PATH = ""


try:
    from .local_config import *
except ImportError:
    pass
