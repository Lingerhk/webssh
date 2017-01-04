# -*- coding: utf-8 -*-

# project: 
# author: s0nnet
# time: 2017-01-03
# desc: webssh


from handlers import *


handlers = [
    (r"/", IndexHandler),
    (r"/ws", WSHandler)
]
