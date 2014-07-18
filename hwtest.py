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
import telnetlib
#import locale
import curses.textpad
import curses.wrapper
import datetime


# start logging function
import datetime
import logging
LOG_FILENAME = 'main.log'
start_time= datetime.datetime.now()
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, )
logging.debug("Running hwtest at " + str(start_time))

# open file descriptor for /dev/null
FNULL=open(os.devnull,'w')
#FTRACE=open("trace.txt",'w')

# Master list of all HW tests
test_list= sorted(["Ethernet", "GSM", "Wifi", "oneWire", "AR429", "CFAST", "USB", "Display", "GPIO", "SSD", "Temperature"], key=lambda s: s.upper())

# save all hardware test threads in this array(?) or collection(?)
hw_threads = []

# definition of fifo queue
q = Queue.Queue()

#defintion of port status  - as dictionary
hw_status = {}			# Use {} to define a dictionary.  Use [] to access dictionary elements

# global vars
BLACK= None
RED=  None
GREEN=  None
YELLOW=  None
BLUE=  None
MAGENTA=  None
CYAN=  None
WHITE=  None
WHITE_ON_MAGENTA= None
WHITE_ON_BLACK= None
debug_print= True
the_screen= None

# Stuff that needed to be run once before the main test code
def initial_setup() :
	try:
		result= subprocess.call("sudo route add default wwan0", shell=True,stdout=FNULL, stderr=FNULL)
		return (result == 0)
	except OSError as e:
		return False



HW_TEST_LINE= 7
HW_TEST_COL= 10+1

def dprint(s) :
	if debug_print :
		the_screen.move(HW_TEST_LINE+len(test_list)+5,0)
		the_screen.insdelln(-1)
		the_screen.addstr(HW_TEST_LINE+len(test_list)+13, 0, s, WHITE)


# --begin oneWire hardware test
#import oneWire

def oneWire_thread():
	try:
		#result= -1		# oneWire.run_test()
		fname= "oneWire.txt"			# add full path for oneWire drive
		fdata = "oneWire tested at " + str(datetime.datetime.now()) + "\n"
		w = open(fname, 'w')
		w.write(fdata)
		w.close()
		r = open(fname, 'r')
		input= r.read(256);			# limit read to 256 bytes
		r.close()
		if input == fdata :
		#result= CFAST.run_test(arg)
		#if result == 0:
			q.put(["oneWire", "Pass"])
		else:	q.put(["oneWire", "Fail"])
		if result == 0:
			q.put(["oneWire", "Pass"])
		else:	q.put(["oneWire", "Fail"])
	except OSError as e:
		q.put(["oneWire", "Not available"])


def start_oneWire_test(arg):
	the_name= "oneWire"
	t1 = Thread(target=oneWire_thread, name= the_name, args=())
	t1.daemon = True
	hw_threads.append(t1)
	t1.start()
# end oneWire test


# --begin AR429 hardware test
#import AR429

def AR429_thread(arg):
	try:
#		result= AR429.run_test(arg)
#		if result == 0:
#			q.put(["AR429", "Pass"])
#		else:	q.put(["AR429", "Fail"])
		time.sleep(0.2)
		q.put(["AR429", "Not implemented"])
	except OSError as e:
		q.put(["AR429", "Not available"])


def start_AR429_test(arg):
	the_name= "AR429 " + str(arg)
	t = Thread(target=AR429_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

# end AR429 test


# --begin CFAST hardware test
#import CFAST

def CFAST_thread(arg):
	try:
		fname= "CFAST.txt"			# add full path for CFAST drive
		fdata = "CFAST tested at " + str(datetime.datetime.now()) + "\n"
		w = open(fname, 'w')
		w.write(fdata)
		w.close()
		r = open(fname, 'r')
		input= r.read(256);			# limit read to 256 bytes
		r.close()
		if input == fdata :
		#result= CFAST.run_test(arg)
		#if result == 0:
			q.put(["CFAST", "Pass"])
		else:	q.put(["CFAST", "Fail"])
	except OSError as e:
		q.put(["CFAST", "Not available"])


def start_CFAST_test(arg):
	the_name= "CFAST " + str(arg)
	t = Thread(target=CFAST_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

# end CFAST test



# --begin USB hardware test
#import USB

def USB_thread(arg):
	try:
#		result= USB.run_test(arg)
#		if result == 0:
#			q.put(["USB", "Pass"])
#		else:	q.put(["USB", "Fail"])
		time.sleep(0.8)
		q.put(["USB", "Not implemented"])
	except OSError as e:
		q.put(["USB", "Not available"])


def start_USB_test(arg):
	the_name= "USB " + str(arg)
	t = Thread(target=USB_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

# end USB test


# --begin solid state flash drive test
def SSD_thread(arg):
	try:
		fname= "SSDFile.txt"			# add full path for each drive
		fdata = "SSD tested at " + str(datetime.datetime.now()) + "\n"
		w = open(fname, 'w')
		w.write(fdata)
		w.close()
		r = open(fname, 'r')
		input= r.read(256);			# limit read to 256 bytes
		r.close()
		if input == fdata :
			q.put(["SSD", "Pass"])
		else:	q.put(["SSD", "Fail"])
	except OSError as e:
		q.put(["SSD_drive", "Not available"])

def start_SSD_test(arg):
	the_name= "SSD " + str(arg)
	t = Thread(target=SSD_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()
# end solid state flash drive test



# --begin Display hardware test (LEDs, E-Ink)
#import Display

def Display_thread(arg):
	try:
#		result= Display.run_test(arg)
#		if result == 0:
#			q.put(["Display", "Pass"])
#		else:	q.put(["Display", "Fail"])
		time.sleep(0.4)
		q.put(["Display", "Not implemented"])
	except OSError as e:
		q.put(["Display", "Error"])


def start_Display_test(arg):
	the_name= "Display " + str(arg)
	t = Thread(target=Display_thread, name= the_name, args=(arg,))
	t.daemon = True
	hw_threads.append(t)
	t.start()

# end Display test


# --begin Temperature hardware test
def Temperature_thread():
	try:
#		s= subprocess.check_output("sensors -f | grep -o \+[0-9]*\.[0-9]*.F[\ ]", shell=True, stdin=None, stderr=None, universal_newlines=False)
#		tlist= s.split("\n")
		result= "Pass"
#		for item in tlist :
			#l= len(item.decode("utf-8")) -2
			#dprint("!! " + item + " has length " + str(l+2))
#			l= len(item) -4			# strip the °F
#			if l > 0 :
#				dprint("!! truncated to " + item[0:l])
#				f= float(item[0:l])
				#dprint("!! " + str(f))
#				if (f < 32) or (f > 132) :
#					result= "Fail"
#		s= s.replace("\n"," ")
		slist= ['37°C', '35°C']
		s1= "CPU " + slist[0] + "   board " + slist[1] + "   disk NA"
		q.put(["Temperature", result + "\t" + s1])
	except  subprocess.CalledProcessError, e:
		q.put(["Temperature", "Not available"])


def start_Temperature_test():
	the_name= "Temperature"
	t1 = Thread(target=Temperature_thread, name= the_name, args=())
	t1.daemon = True
	hw_threads.append(t1)
	t1.start()
# end Temperature test


# --begin digital_IO hardware test
# GPIO testing requires the use of the test computers.  Values are written to the GPIO on one PC
# and read by the other PC.  Ths board test software uses a telnet connection to the test PC
# in order to issue remote read and write gpio commands.
#import GPIO

GPIO_test_values= [0x00000, 0xfffff, 0x55555, 0xaaaaa, 0x33333, 0xccccc]

#HOST= "192.168.0.1"
HOST= "TestComputer"
USER= "anonymous"
PASSWORD= ""

def GPIO_telnet_thread(host, user, password):
	result= True
	try:
		tn = telnetlib.Telnet(host)
		try:
			tn.read_until("login: ")
			tn.write(user + "\n")
			if password:
		    		tn.read_until("Password: ")
				tn.write(password + "\n")
			# test GPIO output
			time.sleep(0.010)
			for value in GPIO_test_values:
				GPIO.write20(value)		# write value to local GPIO port
				time.sleep(0.010)		# delay 10 msec to ensure GPIO bits are set
				tn.write("read_gpio20\n")	# run remote command to read port value
				r= tn.read_some()		# hopefully read complete line
				if int(r) != value:
					result= False
					dprint("GPIO error, output " + hex(value) + "  read " + r)
					break
			# test GPIO input
			time.sleep(0.010)
			for value in GPIO_test_values:
				value&= 3
				tn.write("write_gpio4 " + hex(value)+ "\n")	# run remote command to write port value
				#r= tn.read_some()		# wait for ack
				time.sleep(0.050)		# delay 50 msec to ensure GPIO bits are set
				r= GPIO.read4()			# read local GPIO port
				if r != value:
					result= False
					dprint( "GPIO error, input " + hex(value) + "  read " + r)
					break
		except IOError:
			result= False
			dprint("Telnet read/write failure: " + str(sys.exc_info()))
		finally:
			tn.close()
			if result == True:
				q.put(["GPIO", "Pass"])
			else:
				q.put(["GPIO", "Fail"])

	except IOError:
		#dprint("Telnet open failure: " + str(sys.exc_info()))
		q.put(["GPIO", "Not available"])



def start_GPIO_test(arg):
	the_name= "GPIO_telnet_thread"
	t = Thread(target=GPIO_telnet_thread, name= the_name, args=(HOST, USER, PASSWORD))
	t.daemon = True
	hw_threads.append(t)
	t.start()


# end digital_IO test


# begin ethernet testing
def ethernet_thread(dest):
	#dest= "10.0.2.101"
	#interface= "eth0"
	#q.put(["Ethernet", interface, "Running"])
	#q.put(["Ping", interface, "Running"])
	try:
#		s= subprocess.check_output(["ifconfig", "-s"], stdin=None, stderr=None, shell=True, universal_newlines=False)
		s= subprocess.check_output("ifconfig -s", shell=True, stdin=None, stderr=None, universal_newlines=False)
		#dprint("!" + s)
		elist= re.findall(r'\beth[0-9]*', s)
	except  subprocess.CalledProcessError, e:
		q.put("Ethernet", None)
		elist=[]

	for interface in elist :
		try:
#			ping_result= subprocess.call(["ping", "-c 4 -i 0.25 -I "+ interface, dest],stdout=FNULL, stderr=FNULL)
			ping_result= subprocess.call("ping -c 4 -i 0.25 -I " + interface + " " + dest, shell= True, stdout=FNULL, stderr=FNULL)
			dprint("ethernet ping result = " + str(ping_result))
			if ping_result == 0:
				q.put(["Ethernet", interface, "Pass"])
			else:	q.put(["Ethernet", interface, "Fail"])
		except  subprocess.CalledProcessError, e:
			logging.debug("ethernet failed:", e)
			q.put(["Ethernet", interface, "Not available"])

# end ethernet test

# --begin Wifi hardware test
#import Wifi


# Probably should add these Wifi login parameters to file /etc/network/interfaces
# used by command:  ifup wlan0,   not sure about command: ifconfig wlan0 up
#auto wlan0
#iface wlan0 inet dhcp
#  wpa-ssid mynetworkname
#  wpa-psk mysecretpassphrase


def Wifi_thread(dest):
	try:
		dprint("Begin wifi")
#		s= subprocess.check_output(["ifconfig", "-s"], stdin=None, stderr=None, shell=False, universal_newlines=False)
		s= subprocess.check_output("ifconfig -s", shell=True, stdin=None, stderr=None, universal_newlines=False)
#		s= subprocess.check_output(["iwconfig", " "], stdin=None, stderr=None, shell=False, universal_newlines=False)
		#dprint("!" + s)
		elist= re.findall(r'\bwlan0', s)
	except  subprocess.CalledProcessError, e:
		elist= []
		dprint("iwconfig failed")

	if "wlan0" in elist :
		try:
#			ping_result= subprocess.call(["ping", "-c 4 -i 0.25 -I wlan0",dest],stdout=FNULL, stderr=FNULL)
			ping_result= subprocess.call("ping -c 4 -i 0.25  -I wlan0 " + dest, shell=True,stdout=FNULL, stderr=FNULL)
			dprint("Wlan0 ping result = " + str(ping_result))
			if ping_result == 0:
				q.put(["Wifi", "Pass"])
			else:	q.put(["Wifi", "Fail"])
		except  subprocess.CalledProcessError, e:
			dprint("No Wifi error")
			q.put(["Wifi", "Not available"])

	else :
		dprint("No Wifi detected")
		q.put("Wifi", "Not available")
# end Wifi test


# --begin GSM hardware test
# There may be up to 4 Sim card
# sudo route add default wwan0
#import GSM

def GSM_thread(arg):
	try:
		result= False
		#for card in range(4):			# for each sim card
			#GSM.select_SIM(card)		# select sim card
			#GSM.reboot_chip()		# reboot GSM chip
			#time.sleep(0.500)		# allow time for chip to reset
			#result= GSM.run_test(arg)
			#dprint( "GSM SIM " + str(card) + ": " + str(result))
			#if result == 1:
			#	result= True
			#	break
		result = GSM_ping(arg)
		if result == 0:
			q.put(["GSM", "Pass"])
		else:
			q.put(["GSM", "Fail"])
	except OSError as e:
		q.put(["GSM", "Not available"])


def GSM_ping(dest):
	try:
		ping_result = subprocess.call("ping -c 4 -i 0.25  -I wwan0 " + dest, shell=True,stdout=FNULL, stderr=FNULL)
		dprint("Wwan0 ping result = " + str(ping_result))
		return ping_result
	except  subprocess.CalledProcessError, e:
		dprint("No GSM error")
		q.put(["GSM", "Not available"])
		return -1


#def start_GSM_test(arg):
#	the_name= "GSM " + str(arg)
#	t = Thread(target=GSM_thread, name= the_name, args=(arg,))
#	t.daemon = True
#	hw_threads.append(t)
#	t.start()

# end GSM test


# begin network testing
def switch_to_ethernet() :
	try :
		result= subprocess.call("sudo ifconfig wlan0 down", shell= True, stdout=FNULL, stderr=FNULL)
		if result == 0 :
			result= subprocess.call("sudo ifconfig eth0 up", shell= True, stdout=FNULL, stderr=FNULL)
			if result == 0 :
				return True
	except OSError as e:
		pass
	q.put(["Ethernet", "Not available"])
	return False


def switch_to_wifi() :
	try :
		dprint("! begin switching to wifi")
		result= subprocess.call("nmcli nm wwan off", shell= True, stdout=FNULL, stderr=FNULL)
		result= subprocess.call("sudo ifconfig wwan0 down", shell= True, stdout=FNULL, stderr=FNULL)
		# sudo iwconfig wlan0 key s:password
		result= subprocess.call("nmcli nm wifi on", shell= True, stdout=FNULL, stderr=FNULL)
		result= subprocess.call("sudo ifconfig wlan0 up", shell= True, stdout=FNULL, stderr=FNULL)
		if result == 0 :
			result= subprocess.call("sudo ifconfig eth0 down", shell= True, stdout=FNULL, stderr=FNULL)
		if result == 0 :
			dprint("! wait for switch to wifi")
			i= 20
			while i > 0 :
				i= i -1
				time.sleep(0.500)
				s= subprocess.check_output("iwconfig wlan0", shell=True, stdin=None, stderr=None)
				dprint("waiting for wifi - " + s[0:25])
				if "802.11" in s :
					return True
			dprint("! timeout on switching to wifi")
		else :
			dprint("! ifconfig failed")
	except OSError as e:
		dprint("! Unable to switch to wifi")
		pass
	q.put(["Wifi", "Not available"])
	return False


def switch_to_GSM() :
	return True				# to be completed
	try :
		dprint("! begin switching to gsm")
		result= subprocess.call("nmcli nm wifi off", shell= True, stdout=FNULL, stderr=FNULL)
		result= subprocess.call("sudo ifconfig wlan0 down", shell= True, stdout=FNULL, stderr=FNULL)
		result= subprocess.call("nmcli nm wwan on", shell= True, stdout=FNULL, stderr=FNULL)
		result= subprocess.call("sudo ifconfig wwan0 up", shell= True, stdout=FNULL, stderr=FNULL)
		time.sleep(13)
		result= subprocess.call("nmcli con up id 'AT&T LaptopConnect (data cards) 1'", shell= True, stdout=FNULL, stderr=FNULL)
		if result == 0 :
			result= subprocess.call("sudo ifconfig eth0 down", shell= True, stdout=FNULL, stderr=FNULL)
		if result == 0 :
			dprint("! wait for switch to wifi")
			i= 20
			while i > 0 :
				i= i -1
				#time.sleep(0.500)
				s= subprocess.check_output("iwconfig wwan0", shell=True, stdin=None, stderr=None)
				dprint("waiting for gsm - " + s[0:25])
				if "802.11" in s :
					return True
			dprint("! timeout on switching to wifi")
		else :
			dprint("! ifconfig failed")
	except OSError as e:
		dprint("! Unable to switch to gsm")
		pass
	q.put(["GAM", "Not available"])
	return False


def network_thread(nlist,dest):
	if ("Ethernet" in nlist) and switch_to_ethernet():
		time.sleep(2)
		ethernet_thread(dest)
	if ("Wifi" in nlist) and switch_to_wifi() :
		time.sleep(5 +2)			# must wait 5 seconds or more
		Wifi_thread("google.com")
		switch_to_ethernet()
	if ("GSM" in nlist) and switch_to_GSM() :
		GSM_thread("google.com")
		#switch_to_ethernet()


def start_network_test(nlist, arg) :
	the_name= "network " + arg
	t = Thread(target=network_thread, name= the_name, args=(nlist,arg))
	t.daemon = True
	hw_threads.append(t)
	t.start()

# End network testing


def run_hw_tests(tests):

	now = datetime.datetime.now()
	now = str(now)
	f = open('./hwtest_results.txt', 'w')
	f.write("***********************************************************************\n\n")
	f.write("Test Report: ")
	f.write(now[0:16])
	f.write('\n')
	f.write("-----------------------------------------------------------------------\n")
	f.write("Test				Result\n")
	f.write("-----------------------------------------------------------------------\n")
	f.close()

	def print_test(test) :
		if test in test_list :
			i= test_list.index(test)
			if (i>=0) and (i <= len(test_list)) :
				the_screen.addstr(HW_TEST_LINE+i, 10, "[ ] " +test, WHITE_ON_BLACK | curses.A_BOLD)

	dprint( "Testing " + str(tests))
	arg= "[]"
	nlist=[]
	if "Ethernet" in tests :
		nlist.append("Ethernet")
	if "Wifi" in tests:
		nlist.append("Wifi")
	if "GSM" in tests:
		nlist.append("GSM")
	if nlist != [] :
		print_test("network " + str(nlist))
		start_network_test(nlist, "10.0.2.100")
	if "oneWire" in tests:
		print_test("oneWire")
		start_oneWire_test(arg)
	if "AR429" in tests:
		print_test("AR429")
		start_AR429_test(arg)
	if "CFAST" in tests:
		print_test("CFAST")
		start_CFAST_test(arg)
	if "USB" in tests:
		print_test("USB")
		start_USB_test(arg)
	if "Display" in tests:
		print_test("Display")
		start_Display_test(arg)
	if "GPIO" in tests:
		print_test("GPIO")
		start_GPIO_test(arg)
	if "SSD" in tests:
		print_test("SSD")
		start_SSD_test(arg)
	if "Temperature" in tests:
		print_test("Temperature")
		start_Temperature_test()

	if debug_print :
		the_screen.refresh()


# Each HW test runs in its own thread and sends results back to the main thread via a queue.
def read_q():
	status= True
	while not q.empty():
		m= q.get()
		dprint("++ " + str(m))
		if m[0] == "Ethernet":
			#for interface in m[1]:
			#	hw_status[interface]= "Present"
			#	ping_address(interface, "10.0.2.100")		# Check This address
			#status= False
			hw_status["Ethernet"] = m[2]
		elif m[0] == "Ping":
			hw_status[m[1]] = m[2]
		elif m[0] == "GSM":
			hw_status["GSM"] = m[1]
		elif m[0] == "Wifi":
			hw_status["Wifi"] = m[1]
		elif m[0] == "oneWire":
			hw_status["oneWire"] = m[1]
		elif m[0] == "AR429":
			hw_status["AR429"] = m[1]
		elif m[0] == "CFAST":
			hw_status["CFAST"] = m[1]
		elif m[0] == "GPIO":
			hw_status["GPIO"] = m[1]
		elif m[0] == "USB":
			hw_status["USB"] = m[1]
		elif m[0] == "Display":
			hw_status["Display"] = m[1]
		elif m[0] == "SSD":
			hw_status["SSD"] = m[1]
		elif m[0] == "Temperature" :
			hw_status["Temperature"] = m[1]

		if debug_print :
			if m[0] == "Ethernet":
				print_status(m[0], m[2])
			else :
				print_status(m[0], m[1])
			the_screen.refresh()

	return status


def run_tests(tests):
	the_screen.move(0,0)
	the_screen.clrtoeol()
	the_screen.addstr(0, 0, "Running tests", WHITE_ON_MAGENTA | curses.A_BOLD)
	the_screen.addstr(HW_TEST_LINE-2, 10, "Test results:", WHITE_ON_BLACK | curses.A_BOLD)
	# Start hw test threads
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
				dprint("** Error " + t.getName() + " is still running.")
			break;

	the_screen.addstr(0, 0, "Press space key to toggle tests, tab or arrow keys to move, a to select all, r to run, q to exit", WHITE_ON_MAGENTA | curses.A_BOLD)
	the_screen.refresh()


# screen movement functions
def cursor_up(screen):
	row, col= screen.getyx()
	if row <= HW_TEST_LINE or row > (HW_TEST_LINE + len(test_list) -1) :
		row= (HW_TEST_LINE + len(test_list) -1)
	else :
		row = row-1
	col= HW_TEST_COL
	screen.move(row, col)
	screen.refresh()

def cursor_down(screen):
	row, col= screen.getyx()
	if row < HW_TEST_LINE :
		row= HW_TEST_LINE
	elif row >= (HW_TEST_LINE + len(test_list) -1) :
		row= HW_TEST_LINE
	else :
		row= row+1
	col= HW_TEST_COL
	screen.move(row, col)
	screen.refresh()

def cursor_tab(screen):
	row, col= screen.getyx()
	if row < HW_TEST_LINE :
		row= HW_TEST_LINE
	elif row >= (HW_TEST_LINE + len(test_list) -1) :
		row= HW_TEST_LINE
	else :
		row= row+1
	col= HW_TEST_COL
	screen.move(row, col)
	screen.refresh()

def cursor_backtab(screen):
	row, col= screen.getyx()
	if row <= HW_TEST_LINE :
		row= HW_TEST_LINE + len(test_list) -1
	elif row >= HW_TEST_LINE  +len(test_list) :
		row= HW_TEST_LINE+ len(test_list) -1
	else :
		row= row-1
	col= HW_TEST_COL
	screen.move(row, col)
	screen.refresh()


def cursor_left(screen):
	row0, col0= screen.getbegyx()
	row, col= screen.getyx()
	if col > col0 :
		col= col -1
	screen.move(row, col)
	screen.refresh()

def cursor_right(screen):
	nrows, ncols= screen.getmaxyx()
	row, col= screen.getyx()
	if col < (ncols-1) :
		col= col +1
	screen.move(row, col)
	screen.refresh()


def display_all_tests(screen) :
	for item in test_list:
		row= test_list.index(item)
		screen.addstr(row+HW_TEST_LINE, 10, "[ ] " +item,WHITE_ON_BLACK)
		screen.move(row+HW_TEST_LINE, 10+1)
		screen.addch(row+HW_TEST_LINE, 10+1, curses.ACS_DIAMOND, WHITE_ON_BLACK)
	screen.move(HW_TEST_LINE, 10+1)
	screen.refresh()			# redraw the screen with new output


def print_status(test, result) :
	if test not in test_list :
		return
	if result == None :
		color= WHITE_ON_BLACK
	elif result.startswith("Pass") :
		color= GREEN
	elif result.startswith("Fail") :
		color= RED
	else :
		color= WHITE_ON_BLACK
	i= test_list.index(test)
	if (i>=0) and (i <= len(test_list)) :
		the_screen.move(HW_TEST_LINE+i,0)
		the_screen.clrtoeol()
		the_screen.addstr(HW_TEST_LINE+i, 10, "[ ] " +test, color | curses.A_BOLD)
		f = open('./hwtest_results.txt', 'a')
		f.write(test)
		if result != None :
			the_screen.addstr(HW_TEST_LINE+i, 34, result, color | curses.A_BOLD)
			if len(test) >= 8:
				result_output = "\t\t\t"+result+'\n'
			else:
				result_output = "\t\t\t\t"+result+'\n'
			f.write(result_output)
		f.close()
		the_screen.chgat(HW_TEST_LINE+i, 1, 79, color | curses.A_BOLD)
		curses.textpad.rectangle(the_screen,HW_TEST_LINE-5,0,HW_TEST_LINE+len(test_list)+3,81)


def setup_colors(screen) :
	# setup the given color on black background
	global RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, WHITE_ON_MAGENTA, WHITE_ON_BLACK
	if curses.has_colors() :
		for i in xrange(1 ,curses.COLORS):
			curses.init_pair(i, i, curses.COLOR_BLACK)
		curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
		curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_BLUE)
		#BLACK= curses.color_pair(0)		# color_pair(0) hardwired to white on black
		#WHITE= curses.color_pair(0)
		RED= curses.color_pair(1)
		GREEN= curses.color_pair(2)
		YELLOW= curses.color_pair(3)
		BLUE= curses.color_pair(4)
		MAGENTA= curses.color_pair(5)
		CYAN= curses.color_pair(6)
		WHITE_ON_BLACK= curses.color_pair(7)
		WHITE_ON_MAGENTA= curses.color_pair(8)
		WHITE= curses.color_pair(9)
	else :						# to be complete, almost certainly not needed
		WHITE= curses.color_pair(0)
		RED= curses.color_pair(0)
		GREEN= curses.color_pair(0)
		YELLOW= curses.color_pair(0)
		BLUE= curses.color_pair(0)
		MAGENTA= curses.color_pair(0)
		CYAN= curses.color_pair(0)
		WHITE_ON_BLACK= curses.color_pair(0)
		WHITE_ON_MAGENTA= curses.color_pair(0)


def my_function(stdscr):
	screen = stdscr
	global the_screen
	the_screen = stdscr
	the_screen.attron(curses.A_ALTCHARSET)		# to display curses.ACS_DIAMOND
	#locale.setlocale(locale.LC_ALL, '')
	#the_code = locale.getpreferredencoding()
	#global the_code

	curses.flushinp()			# Flush all input buffers.
	setup_colors(screen)
	screen.erase()
	screen.bkgd(' ', WHITE)

	screen.addstr(0, 0, "Connect all cables and press enter", WHITE_ON_MAGENTA | curses.A_BOLD)
	screen.nodelay(0)			# returns on keypresses
	screen.getch()
	screen.move(0,0)
	screen.clrtoeol()

	curses.textpad.rectangle(screen,HW_TEST_LINE-5,0,HW_TEST_LINE+len(test_list)+3,81)
	for i in range(HW_TEST_LINE-4, HW_TEST_LINE+len(test_list)+3):
		for j in range(1, 80):
			the_screen.addch(i, j, ' ', WHITE_ON_BLACK)

	display_all_tests(screen)		# Not needed
	run_tests(test_list)
	retry_list= []

	#screen.nodelay(0)			# getch returns only when keypresses
	screen.nodelay(1)			# getch returns immediately
	while True:
		time.sleep(0.005)		# sleep 50 ms
		read_q()
		key= screen.getch()
		if key == curses.ERR:		# no keypress
			continue
		elif key == curses.KEY_UP:
			cursor_up(screen)
		elif key == curses.KEY_DOWN:
			cursor_down(screen)
		elif (key == ord('\t')) or (key == ord('\n')):
			cursor_tab(screen)
		elif key == curses.KEY_BTAB:
			cursor_backtab(screen)
		elif key == ord(' '):
			row, col= screen.getyx()
			if (row >= HW_TEST_LINE) and (row <= (HW_TEST_LINE+len(test_list))) :
				t= test_list[row-HW_TEST_LINE]
				if t in retry_list :
					retry_list.remove(t)
					screen.addch(row, col, ' ', WHITE_ON_BLACK)
				else :
					retry_list.append(t)
					screen.addch(row, col, curses.ACS_DIAMOND, WHITE_ON_BLACK)
				cursor_left(screen)
				cursor_tab(screen)
		elif (key == ord('A')) or (key == ord('a')) :
			retry_list=[]
			for item in test_list :
				retry_list.append(item)
			for row in range(HW_TEST_LINE, HW_TEST_LINE+len(test_list)) :
				screen.addch(row, HW_TEST_COL, curses.ACS_DIAMOND, WHITE_ON_BLACK)
			screen.move(HW_TEST_LINE, HW_TEST_COL)

		elif (key == ord('R')) or (key == ord('r')) :
			for item in retry_list:
				hw_status[item]= None
				print_status(item, None)
			screen.refresh()
			run_tests(retry_list)
			retry_list=[]
			#del retry_list[:]		# Clear the list. Slightly more precise than retry_list=[]

		elif (key == ord('Q')) or (key == ord('q')):
			break
		else:
			pass


# Begin here
hw_status.clear()
initial_setup()
curses.wrapper(my_function)
f = open('./hwtest_results.txt', 'a')
f.write("\n***********************************************************************\n")
f.close()

# 1:04pm


