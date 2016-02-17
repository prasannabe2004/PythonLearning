#!/usr/bin/python

# If you dont want to share the pytho code
# use: python -m compileall telnet.py
# This creates telnet.pyc which is a bytecode file

import sys
import telnetlib
import time

password = "simple"
waitTime = 5

HOST="172.16.213.204"
tn = None

def loginSession():
    global tn
    global password
    tn.read_until(b"User Name ")
    tn.write(b"root"+b"\n\r")
    tn.read_until(b"Password")
    tn.write(password + b"\n\r")

def rebootACPU():
    global tn
    global waitTime

    #Lets get into the ACPU Control Menu
    tn.write(b"1\n\r")
    tn.write(b"2\n\r")
    tn.write(b"1\n\r")
    tn.write(b"1\n\r")
    tn.write(b"1\n\r")

    #IMMEDIATE OFF
    tn.write(b"2\n\r")
    tn.write(b"YES\n\r")
    tn.write(b"\n\r")

    #Lets sleep
    print("Waiting for ", waitTime, " seconds...");
    time.sleep(waitTime)

    #IMMEDIATE ON
    tn.write(b"1\n\r")
    tn.write(b"YES\n\r")
    tn.write(b"\n\r")

    #Lets Exit
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"4\n\r")
    lastpost = tn.read_all().decode('ascii')
    print(lastpost)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        waitTime = int(sys.argv[1])
        print("Wait Time is ", waitTime )
    else:
        print("Defaulting to ", waitTime)
    tn = telnetlib.Telnet(HOST)
    tn.set_debuglevel(1)
    loginSession()
    rebootACPU()
    sys.exit(0)

