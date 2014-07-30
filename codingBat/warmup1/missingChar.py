# Assignments from http://codingbat.com/
# Warmup1

def missingChar(my_str,n):
	front=my_str[0:n]
	back=my_str[n+1:]
	return front+back

a = missingChar("Prasanna",int(7))

print("Result = "+str(a))