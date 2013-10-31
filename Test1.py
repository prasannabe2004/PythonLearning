import math
import sys
name = "Prasanna"
n = 0
while n < 3:
	
	input = str(raw_input("Enter the name "))
	if name == input:
		print "Match Found"
		sys.exit()
	else:
		print "Try again"
	n = n + 1

