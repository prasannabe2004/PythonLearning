#!/usr/bin/python

def TestRead():
	try:
		fh = open("testfile", "r")
		data = fh.read(100)
	except IOError:
		print ("Error: can\'t find file or read data")
	else:
		print ("Read contents from the file successfully\n"+data)
		fh.close()

def TestWrite():
	try:
		fh = open("testfile", "w")
		fh.write("This is my test file for exception handling!!")
	except IOError:
		print ("Error: can\'t find file or read data")
	else:
		print ("Written content in the file successfully")
		fh.close()

TestRead()
TestWrite()
TestRead()