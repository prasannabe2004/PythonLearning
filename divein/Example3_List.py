#!/usr/bin/python

my_list = ["server","mpilgrim","database","master"]

#Print the list
print my_list

# Accessing the list
print my_list[0],my_list[1]

# Negative Indexing
print my_list[-1],my_list[-2]

#Slicing the list
print my_list[1:3]
print my_list[1:-1]

#Slicing in shorthand
print my_list[:3]
print my_list[3:]
print my_list[:]

#Adding elements to the list
my_list.append("Bye")
my_list.insert(0,"Hello")
my_list.extend(["extn1"])

print my_list
