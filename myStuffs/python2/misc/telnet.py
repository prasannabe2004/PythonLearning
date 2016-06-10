#!/usr/bin/python

# If you dont want to share the pytho code
# use: python -m compileall telnet.py
# This creates telnet.pyc which is a bytecode file

import sys
import telnetlib
import time

password = "simple"
waitTime = 2
iterations = 3

HOST = "172.16.213.10"
tn = None


def login_session():
    global tn
    global password
    try:
        tn.read_until(b"User Name ")
        tn.write(b"root"+b"\n\r")
        tn.read_until(b"Password")
        tn.write(password + b"\n\r")
    except:
        print("Unable to connect")


def reboot_acpu():
    global tn
    global waitTime

    #Lets get into the ACPU Control Menu
    tn.write(b"1\n\r")
    tn.write(b"2\n\r")
    tn.write(b"1\n\r")
    tn.write(b"1\n\r")
    tn.write(b"1\n\r")

    #IMMEDIATE OFF
    #tn.write(b"2\n\r")
    #tn.write(b"YES\n\r")
    #tn.write(b"\n\r")

    #Lets sleep
    print("Waiting for ", waitTime, " seconds...")
    time.sleep(waitTime)

    #IMMEDIATE ON
    #tn.write(b"1\n\r")
    #tn.write(b"YES\n\r")
    #tn.write(b"\n\r")

    #Lets Exit
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"\x1b\r")
    tn.write(b"4\n\r")
    #last_post = tn.read_all().decode('ascii')
    #print(last_post)


if __name__ == "__main__":
    i = 0
    if len(sys.argv) == 3:
        waitTime = int(sys.argv[1])
        iterations = int(sys.argv[2])
        print("Wait Time is ", waitTime)
        print("Number of iterations is ", iterations)
    else:
        print("Defaulting to ", waitTime)
        print("Defaulting to ", iterations)
    while i < iterations:
        print("Starting Iteration ", i)
        tn = telnetlib.Telnet(HOST)
        tn.set_debuglevel(1)
        login_session()
        reboot_acpu()
        i += 1
    sys.exit(0)

