# -*- coding: utf-8 -*-

# project: 
# author: s0nnet
# time: 2017-01-03
# desc: webssh


import os.path

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import options

from config import init_config
from urls import handlers
from ioloop import IOLoop


settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)


class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    init_config()
    options.parse_config_file("webssh.conf")

    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    IOLoop.instance().start()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
