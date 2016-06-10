import sys
import threading
import time
import subprocess
import myStuffs.python2.random
import copy
import os
import signal
import datetime
from time import gmtime, strftime

max_url_count = 50000
urls = []

terminate = False

urllock = None
removed_urls = []

good_urls = []

###
resultslog = open('results.txt', 'a')
###

class User(threading.Thread):
	def __init__(self, userno):
		threading.Thread.__init__(self)
		self.userno = userno

	def run(self):
		global urls
		global terminate
		global urllock

		print "Starting user", self.userno

		with urllock:
			my_urls = copy.copy(urls)
		myStuffs.python2.random.shuffle(my_urls)
		nulldev = open(os.devnull, 'w')
		while not terminate:
			for url in my_urls:
				if terminate:
					break

				start = time.time()

				#p = subprocess.Popen(('wget -p --cache=off  --delete-after -T 5 -t 1 ' + url).split(), stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=False)
				#p = subprocess.Popen(('wget -p --cache=off  --delete-after -T 10 -t 1 ' + url).split(), stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=False)
				p = subprocess.Popen(('wget -r -l 1 -p --cache=off  --delete-after -T 10 -t 1 ' + url).split(), stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=False)

				errstring = p.communicate()[1]
				rc = p.returncode

				end = time.time()
				if rc == 0:
					resultslog.write('%.2fs\t%s' % (end - start, url))
					print '%.2fs\t%s' % (end - start, url)
				else:
					resultslog.write('err %i\t%s' % (rc, url))
					print 'err %i\t%s' % (rc, url)
                                #print (time.strftime("%H:%M:%S"))
				time.sleep(60)
                                #print (time.strftime("%H:%M:%S"))
				if rc == 0:
					with urllock:
						try:
							if url not in good_urls:
								good_urls.append(url)
						except:
							pass

				if rc == 4:
					with urllock:
						try:
							print '>>>>>>>>removing', url
							urls.remove(url)
							removed_urls.append(url)
						except:
							pass


def signal_handler(signal, frame):
	print 'Terminating, pls wait...!'
	global terminate
	terminate = True


if __name__ == '__main__':
	# How many users?
	usercount = 1
	if len(sys.argv) >= 2:
		usercount = int(sys.argv[1])

	urlfile = 'urls.txt'
	#urlfile = 'inurl.txt'
	if len(sys.argv) >= 3:
		urlfile = sys.argv[2]


	# Read some url's
	f = open(urlfile, 'r')
	for line in f:
		if len(urls) >= max_url_count:
			break
		urls.append(line)

	urllock = threading.Lock()

	signal.signal(signal.SIGINT, signal_handler)

	# Start thread per user
	users = []
	for userno in range(1, usercount + 1):
		user = User(userno)
		user.start()
		users.append(user)

	while not terminate:
		time.sleep(1)

	for user in users:
		user.join()

	f = open('cleaned' + urlfile, 'w')
	for url in urls:
		f.write(url)

	f = open('good_urls.txt', 'w')
	for url in good_urls:
		f.write(url)
	
	print 'removed', len(removed_urls), 'urls'
	print 'good urls', len(good_urls)
