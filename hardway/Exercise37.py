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

def start():
	test_and_keyword()
	print
	test_del_keyword()

start()