# coding: utf-8
import tornado.gen
from apps.base import BaseHandler


class TestHandler(BaseHandler):
    """
    test
    """
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        data = {"result": True}
        yield self.write_resp(data=data, status=0)