import urllib

def read_test():
	file = open("/home/prasanna/Quotes.txt")
	contents = file.read()
	file.close()
	check_file(contents)

def check_file(contents):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+contents)
	output = connection.read()
	print (output)
	connection.close()
	if "true" in output:
		print("Profanity alert!!!")
	elif "false" in output:
		print("No Profanity")
	else:
		print("unknown")
read_test()
