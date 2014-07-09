#Python 2.7.0

def test_and_keyword():
	x = True
	y = False
	if x == True and y == False:
		print "'and' keyword tested successfully"
	else:
		print "test failed"

def test_del_keyword():
	a = [1,2,3,4,5,6]
	del a[3]
	del a[2:4]
	print "'del' keyword tested successfully", a

def test_import_keyword():
	import myfunctions
	myfunctions.testfunction()
	print "'import' keyword tested successfully"

def test_from_keyword():
	from myfunctions import *
	testfunction()
	print "'from' keyword tested successfully"

def start():
	test_and_keyword()
	print
	test_del_keyword()
	print
	test_import_keyword()
	print
	test_from_keyword()
		

start()