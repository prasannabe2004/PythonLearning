#!/usr/bin/python

import os
import myStuffs.python2.socket
import threading
import datetime
import time

UDP_IP = "0.0.0.0"
#UDP_PORT = 5
UDP_PORT = 53

SERVER_IP = "10.240.19.29"
SERVER_PORT =53 

counter = 0
recv_counter = 0

class RecvThread(threading.Thread):
    def __init__(self,sock):
        threading.Thread.__init__(self)
        self.sock = sock
	self.counter = 0
	self.recv_counter = 0


    def run(self):
        while True:
           data, addr = self.sock.recvfrom(1024)
           current_time = datetime.datetime.utcnow()
           d = data.split("-")
           self.recv_counter = int(d[0])
           sent_time = datetime.datetime.utcnow().strptime(d[1],"%c")
           print d[1], "--", self.recv_counter,  "--", (current_time - sent_time).microseconds


sock = myStuffs.python2.socket.socket(myStuffs.python2.socket.AF_INET,  # Internet
                     myStuffs.python2.socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

r = RecvThread(sock)
r.start()

while True: 
    send_data  = str(counter) + "-" + datetime.datetime.utcnow().strftime("%c")
    counter = counter + 1
    sock.sendto(send_data, (SERVER_IP, SERVER_PORT)) 
    time.sleep(2)

