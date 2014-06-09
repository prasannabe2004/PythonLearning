# Assignments from http://codingbat.com/
# Warmup1

def sleep_in(weekday,vacation):
	if not weekday or vacation :
		return True
	else:
		return False

a = sleep_in(False,True)

print("result = "+str(a))