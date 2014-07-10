#Python 2.7.0

from myfunctions2 import *

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
	testfunction2()
	print "'from' keyword tested successfully"

def test_not_keyword():
	x = True
	print "'not' keyword tested successfully" , not x

def test_while_keyword():
	i = 1;
	while(i<=2):
		print i,
		i = i+1
	print "'while' keyword tested successfully"	

def test_if_elif_else_keywords():
	input = raw_input("Are you a Python Programmer: ")
	if (input == "Yes" or input == "yes" or input == "Y" or input == "y"):
		print "I like you"
	elif (input == "No" or input == "no" or input == "N" or input == "n"):
		print "Why are you here"
	else:
		print "Invalid input"

def start():
	"""
	Test the documentation
	"""
	test_and_keyword()
	test_del_keyword()
	test_import_keyword()
	test_from_keyword()
	test_not_keyword()		
	test_while_keyword()
	test_if_elif_else_keywords()

start()