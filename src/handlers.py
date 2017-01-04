# -*- coding: utf-8 -*-

# project: 
# author: s0nnet
# time: 2017-01-03
# desc: webssh



import logging
import threading

import tornado.web
import tornado.websocket

from tornado.options import options
from daemon import Bridge
from data import ClientData
from sendmail import Semail
from utils import check_ip, check_port


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")


class WSHandler(tornado.websocket.WebSocketHandler):

    clients = dict()
    options.parse_config_file("webssh.conf")

    def get_client(self):
        return self.clients.get(self._id(), None)

    def put_client(self):
        bridge = Bridge(self)
        self.clients[self._id()] = bridge

    def remove_client(self):
        bridge = self.get_client()
        if bridge:
            bridge.destroy()
            del self.clients[self._id()]

    @staticmethod
    def _check_init_param(data):
        if(data["xcode"] != options.xcode):
            logging.warning("xcode error: %s" %(data["xcode"]))
            return False
        return check_ip(data["hostname"]) and check_port(data["port"])

    @staticmethod
    def _is_init_data(data):
        return data.get_type() == 'init'

    @staticmethod
    def _send_email(title, content):
        email = Semail()
        args = (title, content, )
        send = threading.Thread(target= email.send_email, args=args)
        send.start()

    def _id(self):
        return id(self)

    def open(self):
        self.put_client()

    def on_message(self, message):
        bridge = self.get_client()
        client_data = ClientData(message)
        if self._is_init_data(client_data):
            if self._check_init_param(client_data.data):
                bridge.open(client_data.data)
                if(options.smail):
                    msg = "New connect: %s, id: %s, info: %s" % (self.request.remote_ip, self._id(), str(client_data.data))
                    self._send_email("webssh login SUCC", msg)
                logging.info('connection established from: %s' % self._id())
            else:
                self.remove_client()
                msg = "Connect test: %s, info: %s" % (self.request.remote_ip, str(client_data.data))
                self._send_email("webssh login Fail", msg)
                logging.warning('init param invalid: %s' % client_data.data)
        else:
            if bridge:
                bridge.trans_forward(client_data.data)

    def on_close(self):
        self.remove_client()
        logging.info('client close the connection: %s' % self._id())
