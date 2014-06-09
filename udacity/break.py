import webbrowser
import time
while True:
	print(time.ctime())
	time.sleep(6)
	print("Invoking a web browser")
	webbrowser.open("http://facebook.com")
	
