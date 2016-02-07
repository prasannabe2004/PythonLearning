# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:06:24 2015

@author: PMohanasundaram
"""

import socket

cli_socket = socket.socket()

cli_socket.connect(('localhost',50000))


send_data = "Hello server"

cli_socket.send(bytes(send_data,"UTF-8"))

print cli_socket.recv(4096).decode("UTF-8")