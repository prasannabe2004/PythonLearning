# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:00:34 2015

@author: PMohanasundaram
"""

import socket

ser_socket = socket.socket()

ser_socket.bind(('localhost',50000))

ser_socket.listen(10)

conn, addr = ser_socket.accept()

while True:
    print(conn.recv(4096).decode("UTF-8"))
    conn.send(bytes("Hello client","UTF-8"))
