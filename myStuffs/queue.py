#!/usr/bin/python

import Queue
import curses.wrapper

def push(queueid,num):
    queueid.put(num)

def pull(queueid):
    return queueid.get()

def myfunction(stdscr):
    print "Hello my function"

if __name__ == '__main__':
    print "Main Function"
    myq = Queue.Queue()
    curses.wrapper(myfunction)
    push(myq,"100")
    a = pull(myq)
    print "value is ", a
else:
    print "Unknown"

