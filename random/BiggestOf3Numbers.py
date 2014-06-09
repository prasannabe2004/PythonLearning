# Find the greatest of three numbers

a = int(input("Enter the first number:"))
print (a)
print (type(a))

b = int(input("Enter the second number:"))
print(b)
type(b)

c = int(input("Enter the third number:"))
print(c)

if a>b and a>c :
	print ("a is greatest")
elif b>a and b>c :
	print ("b is greatest")
elif c>a and c>b :
	print ("c is greatest")
else:
	print ("none")