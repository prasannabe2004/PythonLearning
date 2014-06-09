# Leap Year finder

in_year = input("Enter the year:")
print("The input year is "+ str(in_year))

if in_year%4 == 0:
	if in_year%100 ==0:
		if in_year%400 ==0:
			print("year is leap")
		else:
			print("year ia not leap")
	else:
		print("year is leap")
else:
	print("year is not leap")

