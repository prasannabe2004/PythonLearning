# Guess the Number

from random import randint
import math

for i in range(1,6):

	in_num = input("Enter the number:")
	print("input number is " + str(in_num))

	rand_in = randint(1,20)
	print("random number is " + str(rand_in))

	if rand_in > in_num :
		print("Your guess is low")
	elif rand_in < in_num :
		print("Your guess is high")
	else:
		print("Your guess is correct")
		break
else:
	print("You retry exceeded")

