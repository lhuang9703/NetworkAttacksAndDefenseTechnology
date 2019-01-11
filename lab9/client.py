#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 lhuang <lhuang9703@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import socket
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, 
                    default='10.211.55.12', 
                    help='host you want to run this server')
parser.add_argument('--port', type=int, 
                    default=2333, 
                    help='port number')
args = parser.parse_args()

HOST = args.host
PORT = args.port


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        data = raw_input("commands to be executed:")
        if data == 'exit':
            break
        if data is not None:
            s.send(data)
            result = s.recv(23333)
            print result
    s.close()
