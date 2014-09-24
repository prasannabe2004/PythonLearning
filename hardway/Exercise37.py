#!/usr/bin/python
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
    user_input = raw_input("Are you a Python Programmer: ")
    if (user_input == "Yes" or user_input == "yes" or user_input == "Y" or user_input == "y"):
        print "I like you"
    elif (user_input == "No" or user_input == "no" or user_input == "N" or user_input == "n"):
        print "Why are you here"
    else:
    print "Invalid input"


def test_global_keyword():
    global value
    value = 1000


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
    test_global_keyword()
    print value


start()