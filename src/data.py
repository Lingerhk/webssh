# -*- coding: utf-8 -*-

# project: 
# author: s0nnet
# time: 2017-01-03
# desc: webssh

import json


class BaseData(object):

    def __init__(self, data=""):
        self.from_json(data)

    def from_json(self, data=""):
        self.__dict__ = json.loads(data)

    def to_json(self):
        return json.dumps(self)

    def get_type(self):
        return self.tp


class ClientData(BaseData):

    def __init__(self, data=""):
        super(ClientData, self).__init__(data)


class ServerData(BaseData):

    def __init__(self, data=""):
        self.tp = 'server'
        self.data = data
