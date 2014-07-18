# -*- coding: utf-8 -*-			# recomended but doesn't fully work
import sys
reload(sys)				# not entirely a good practice to make 
sys.setdefaultencoding("utf-8")		# this work without an exception
import subprocess
import os
from threading import Thread
import threading
import Queue
import time
import re
import datetime


# Master list of all HW tests
test_list= sorted(["Worker1", "Worker2", "Worker3", "USB", "Display", "GPIO", "SSD", "Temperature"], key=lambda s: s.upper())

# save all hardware test threads in this array(?) or collection(?)
hw_threads = []

# definition of fifo queue
q = Queue.Queue()

#defintion of port status  - as dictionary
hw_status = {}			# Use {} to define a dictionary.  Use [] to access dictionary elements

def Worker1_thread():
	print "Worker1 Thread started"
	try:
		if True :
			time.sleep(5)
			q.put(["Worker1", "Pass"])
		else:
			q.put(["Worker1", "Fail"])
	except OSError as e:
		q.put(["Worker1", "Not available"])


def start_Worker1_test(arg):
	the_name= "Worker1"
	t1 = Thread(target=Worker1_thread, name= the_name, args=())
	t1.daemon = True
	hw_threads.append(t1)
	t1.start()

def Worker2_thread(arg):
	print "Worker2 Thread started"
	try:
		time.sleep(4)
		q.put(["Worker2", "Not implemented"])
	except OSError as e:
		q.put(["Worker2", "Not available"])


def start_Worker2_test(arg):
	the_name= "Worker2 " + str(arg)
	t = Thread(target=Worker2_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

def Worker3_thread(arg):
	print "Worker3 Thread started"
	try:
		time.sleep(3)
		if True:
			q.put(["Worker3", "Pass"])
		else:	
			q.put(["Worker3", "Fail"])
	except OSError as e:
		q.put(["Worker3", "Not available"])


def start_Worker3_test(arg):
	the_name= "Worker3 " + str(arg)
	t = Thread(target=Worker3_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

def USB_thread(arg):
	print "USB Thread started"
	try:
		time.sleep(2)
		q.put(["USB", "Not implemented"])
	except OSError as e:
		q.put(["USB", "Not available"])


def start_USB_test(arg):
	the_name= "USB " + str(arg)
	t = Thread(target=USB_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

def SSD_thread(arg):
	print "SSD Thread started"
	try:
		time.sleep(1)
		if True :
			q.put(["SSD", "Pass"])
		else:
			q.put(["SSD", "Fail"])
	except OSError as e:
		q.put(["SSD_drive", "Not available"])

def start_SSD_test(arg):
	the_name= "SSD " + str(arg)
	t = Thread(target=SSD_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

def Display_thread(arg):
	print "Display Thread started"
	try:
		time.sleep(6)
		q.put(["Display", "Not implemented"])
	except OSError as e:
		q.put(["Display", "Error"])


def start_Display_test(arg):
	the_name= "Display " + str(arg)
	t = Thread(target=Display_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

def Temperature_thread():
	print "Temperature Thread started"
	try:
		time.sleep(7)
		if True :
			q.put(["Temperature", "Pass"])
		else:
			q.put(["Temperature", "Fail"])
	except OSError as e:
		q.put(["Temperature", "Not available"])


def start_Temperature_test():
	the_name= "Temperature"
	t1 = Thread(target=Temperature_thread, name= the_name, args=())
	t1.daemon = True
	hw_threads.append(t1)
	t1.start()

def run_hw_tests(tests):
	print "Lets run_hw_tests"
	arg= "[]"
	nlist=[]
	if "Worker1" in tests:
		start_Worker1_test(arg)
	if "Worker2" in tests:
		start_Worker2_test(arg)
	if "Worker3" in tests:
		start_Worker3_test(arg)
	if "USB" in tests:
		start_USB_test(arg)
	if "Display" in tests:
		start_Display_test(arg)
	if "SSD" in tests:
		start_SSD_test(arg)
	if "Temperature" in tests:
		start_Temperature_test()

# Each HW test runs in its own thread and sends results back to the main thread via a queue.
def read_q():
	status= True
	while not q.empty():
		m= q.get()
		if m[0] == "Worker1":
			print "Worker1 completed"
			hw_status["Worker1"] = m[1]
		elif m[0] == "Worker2":
			print "Worker2 completed"
			hw_status["Worker2"] = m[1]
		elif m[0] == "Worker3":
			print "Worker3 completed"
			hw_status["Worker3"] = m[1]
		elif m[0] == "USB":
			print "USB completed"
			hw_status["USB"] = m[1]
		elif m[0] == "Display":
			print "Display completed"
			hw_status["Display"] = m[1]
		elif m[0] == "SSD":
			print "SSD completed"
			hw_status["SSD"] = m[1]
		elif m[0] == "Temperature" :
			print "Temperature completed"
			hw_status["Temperature"] = m[1]
	return status


def run_tests(tests):
	print "run_tests"
	run_hw_tests(tests)
	# Wait for all threads to complete
	timeout= 30				# wait up to 30 seconds
	while threading.activeCount() > 1 :	# wait for all threads (except main) to complete
		time.sleep(0.100)	# sleep 100 ms
		timeout = timeout - 0.100
		read_q()		# read pending results
		if timeout < 0 :		# out of time
			for t in threading.enumerate() :
				if t is threading.currentThread() :
					continue
			break;

def my_function():
	print "my_function"
	run_tests(test_list)

# Begin here
print "HW Test Started"

hw_status.clear()
my_function()



