# coding: utf-8

import tornado.web
import json


class BaseHandler(tornado.web.RequestHandler):
    """
    base handler
    """
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def write_resp(self, data, error_msg="", status=1, **kwargs):
        data = {"data": data}
        data.update(kwargs)
        data.update({"status": status})
        data.update({"error_msg": error_msg})

        self.set_header("Content-Type", "application/json")
        res = json.dumps(data)

        self.finish(res)
