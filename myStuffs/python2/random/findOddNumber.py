# Find a odd number from a list

a = [2,4,7,8,21,12,16]

for i in a:
	if i%2 == 1:
		print (i)
		break
	else:
		print ("i is not a odd number")
		pass
else:
	print ("Could not find any odd numbers")

