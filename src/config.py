# -*- coding: utf-8 -*-

# project: 
# author: s0nnet
# time: 2017-01-03
# desc: webssh

from tornado.options import define


def init_config():
    define('port', default=9520, type=int, help='server listening port')
    define('xcode', default="!@#+%&?", type=str, help='basic pass key')

    define('smail', default=False, type=bool, help='is send email')
    define('username', default="", type=str, help='send mail username')
    define('password', default="", type=str, help='send mail password')
    define('smtpaddr', default="", type=str, help='smtp server address')
    define('smtpport', default=25, type=int, help='smtp server port')
    define('fromaddr', default="", type=str, help='send mail from user')
    define('toaddrs', default="", type=str, help='send mail to user list')

