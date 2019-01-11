#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 lhuang <lhuang9703@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import commands
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
    s.bind((HOST,PORT))
    s.listen(5)
    print('server set up...')

    client_s, client_addr = s.accept()

    while True:
        data = client_s.recv(1024)
        result = commands.getstatusoutput(data)
        print(result[0])
        client_s.send('result of ' + data + ':\n' + result[1] + '\n')

    client_s.close()
    s.close()
