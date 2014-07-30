# Assignments from http://codingbat.com/
# Warmup1

def makes10(a, b):
	if a == 10 or b== 10 or a+b == 10 :
		return True
	else:
		return False


a = makes10(9,10)
print("Result = "+str(a))

a = makes10(9,9)
print("Result = "+str(a))

a = makes10(1,9)
print("Result = "+str(a))