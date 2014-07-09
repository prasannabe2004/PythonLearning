#Python 2.7.0


def test_del_keyword():
	a = [1,2,3,4,5,6]
	print a
	del a[3]
	print a
	del a[2:4]
	print a

def start():
	test_del_keyword()

start()