# Assignments from http://codingbat.com/
# Warmup1

def notString(name):
	print (name[:3])
	if name[:3] != 'not':
		return 'not '+name
	else:
		return name

a = notString('candy')
print("Result = "+str(a))

a = notString('x')
print("Result = "+str(a))

a = notString('not bad')
print("Result = "+str(a))