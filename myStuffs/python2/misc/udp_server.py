#!/usr/bin/python

import os
import myStuffs.python2.socket


import myStuffs.python2.socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5006

sock = myStuffs.python2.socket.socket(myStuffs.python2.socket.AF_INET,  # Internet
                     myStuffs.python2.socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = data + "-ack"
    sock.sendto(data,addr)

