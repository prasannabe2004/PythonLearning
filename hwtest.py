#!/usr/bin/python
#Python 2.7.0

from threading import Thread
import threading
import Queue
import time

# Master list of all HW tests
test_list= sorted(["Worker1", "Worker2", "Worker3", "Worker4", "Worker5", "Worker6", "Worker7", "Worker8"], key=lambda s: s.upper())

# save all hardware test threads in this array(?) or collection(?)
hw_threads = []

# definition of fifo queue
q = Queue.Queue()

#defintion of port status  - as dictionary
hw_status = {}			# Use {} to define a dictionary.  Use [] to access dictionary elements

# Worker1 Thread
def Worker1_thread(arg):
	print "Worker1 Thread started"
	try:
		if True :
			time.sleep(1)
			q.put(["Worker1", "Pass"])
		else:
			q.put(["Worker1", "Fail"])
	except OSError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		q.put(["Worker1", "Not available"])
def start_Worker1_test(arg):
	the_name= "Worker1"
	t1 = Thread(target=Worker1_thread, name= the_name, args=(arg,))
	t1.daemon = True
	hw_threads.append(t1)
	t1.start()

# Worker2 Thread
def Worker2_thread(arg):
	print "Worker2 Thread started"
	try:
		time.sleep(2)
		q.put(["Worker2", "Not implemented"])
	except OSError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		q.put(["Worker2", "Not available"])
def start_Worker2_test(arg):
	the_name= "Worker2 " + str(arg)
	t = Thread(target=Worker2_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

# Worker3 Thread
def Worker3_thread(arg):
	print "Worker3 Thread started"
	try:
		time.sleep(3)
		if True:
			q.put(["Worker3", "Pass"])
		else:	
			q.put(["Worker3", "Fail"])
	except OSError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		q.put(["Worker3", "Not available"])
def start_Worker3_test(arg):
	the_name= "Worker3 " + str(arg)
	t = Thread(target=Worker3_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

# Worker4 Thread
def Worker4_thread(arg):
	print "Worker4 Thread started"
	try:
		time.sleep(4)
		q.put(["Worker4", "Not implemented"])
	except OSError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		q.put(["Worker4", "Not available"])
def start_Worker4_test(arg):
	the_name= "Worker4 " + str(arg)
	t = Thread(target=Worker4_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

# Worker5 Thread
def Worker5_thread(arg):
	print "Worker5 Thread started"
	try:
		time.sleep(5)
		q.put(["Worker5", "Not implemented"])
	except OSError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		q.put(["Worker5", "Error"])
def start_Worker5_test(arg):
	the_name= "Worker5 " + str(arg)
	t = Thread(target=Worker5_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

def Worker6_thread(arg):
	print "Worker6 Thread started"
	try:
		time.sleep(6)
		if True :
			q.put(["Worker6", "Pass"])
		else:
			q.put(["Worker6", "Fail"])
	except OSError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		q.put(["Worker6_drive", "Not available"])

def start_Worker6_test(arg):
	the_name= "Worker6 " + str(arg)
	t = Thread(target=Worker6_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

# Worker7 Thread
def Worker7_thread(arg):
	print "Worker7 Thread started"
	try:
		time.sleep(7)
		if True :
			q.put(["Worker7", "Pass"])
		else:
			q.put(["Worker7", "Fail"])
	except OSError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		q.put(["Worker7", "Not available"])
def start_Worker7_test(arg):
	the_name= "Worker7"
	t1 = Thread(target=Worker7_thread, name= the_name, args=(arg,))
	t1.daemon = True
	hw_threads.append(t1)
	t1.start()

def Worker8_Thread(arg):
	print "Worker8 Thread started"
	try:
		time.sleep(8)
		if True :
			q.put(["Worker8", "Pass"])
		else:
			q.put(["Worker8", "Fail"])
	except OSError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		q.put(["Worker8", "Not available"])

def start_Worker8_test(arg):
	the_name = "Worker8"
	t1 = Thread(target=Worker8_Thread, name = the_name, args=(arg,))
	t1.daemon = True
	hw_threads.append(t1)
	t1.start()

def run_hw_tests(tests):
	arg= "[]"
	if "Worker1" in tests:
		start_Worker1_test(arg)
	if "Worker2" in tests:
		start_Worker2_test(arg)
	if "Worker3" in tests:
		start_Worker3_test(arg)
	if "Worker4" in tests:
		start_Worker4_test(arg)
	if "Worker5" in tests:
		start_Worker5_test(arg)
	if "Worker6" in tests:
		start_Worker6_test(arg)
	if "Worker7" in tests:
		start_Worker7_test(arg)
	if "Worker8" in tests:
		start_Worker8_test(arg)

	#print hw_threads

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
		elif m[0] == "Worker4":
			print "Worker4 completed"
			hw_status["Worker4"] = m[1]
		elif m[0] == "Worker5":
			print "Worker5 completed"
			hw_status["Worker5"] = m[1]
		elif m[0] == "Worker6":
			print "Worker6 completed"
			hw_status["Worker6"] = m[1]
		elif m[0] == "Worker7" :
			print "Worker7 completed"
			hw_status["Worker7"] = m[1]
	return status

def run_tests(tests):
	run_hw_tests(tests)
	# Wait for all threads to complete
	# timeout= 30				# wait up to 30 seconds
	while threading.activeCount() > 1 :	# wait for all threads (except main) to complete
		#time.sleep(0.100)	# sleep 100 ms
		#timeout = timeout - 0.100
		read_q()		# read pending results
		#if timeout < 0 :		# out of time
		#	for t in threading.enumerate() :
		#		if t is threading.currentThread() :
		#			continue
		#	break;

def my_function():
	run_tests(test_list)

print "HW Test Started"

hw_status.clear()
my_function()

print hw_status



