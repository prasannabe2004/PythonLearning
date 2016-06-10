#!/usr/bin/python

import thread
import time
import threading

count = 0

# Define a function for the thread
def print_time( threadName, delay):
	global count
	lock = thread.allocate_lock()
	while count < 50:
		time.sleep(delay)
		lock.acquire()
		count += 1
		lock.release()
		print "%s: %s %d" % ( threadName, time.ctime(time.time()), count )

# Create two threads as follows
try:
	thread.start_new_thread( print_time, ("Thread-1", 2, ) )
	thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
	print "Error: unable to start thread"

while 1:
	pass