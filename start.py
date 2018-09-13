# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
from urls import urls
from config.config import PROJECT_CONFIG

try:
    from config.settings import settings
except ImportError:
    raise ImportError("settings not satisfied")


def make_app():
    _app = tornado.web.Application(
        urls,
        debug=PROJECT_CONFIG["debug"],
        **settings
    )
    return _app


app = make_app()

host = PROJECT_CONFIG["host"]
port = PROJECT_CONFIG["port"]

print("####################")
print("tornado web service start!")
print("running on {}:{}".format(host, port))
print(urls)

app.listen(port, address=host)
tornado.ioloop.IOLoop.current().start()
