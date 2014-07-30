# Assignments from http://codingbat.com/
# Warmup1

def posNeg(a, b, c):
	if c :
		if a < 0 and b < 0:
			return True
	if a < 0 or b < 0:
		return True
	else:
		return False

a = posNeg(1,-1,False)
print("Result = "+str(a))

a = posNeg(1,1,False)
print("Result = "+str(a))

a = posNeg(-1,1,True)
print("Result = "+str(a))