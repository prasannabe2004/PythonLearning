# Python Functions

t=20

def function(a,b,c=None):
	#t=10
	return t+a*2, t+b*2, t+c*2

a,b,c = function(2,3,4)
x,y = function(10,20)

print(a,b,c,x,y)