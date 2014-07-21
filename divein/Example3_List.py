#!/usr/bin/python

my_list = ["server","mpilgrim","database","master"]

print "Print the list"
print my_list

print "Accessing the list"
print my_list[0],my_list[1]

print "Negative Indexing"
print my_list[-1],my_list[-2]

print "Slicing the list"
print my_list[1:3]
print my_list[1:-1]

print"Slicing in shorthand"
print my_list[:3]
print my_list[3:]
print my_list[:]

print "Adding elements to the list"
my_list.append("Bye")

print "Inserting elements to the list"
my_list.insert(0,"Hello")

print "Add two list"
my_list.extend(["extn1"])
print my_list

#Difference between append and extend
#my_list.append(["append1","append2"])
#print my_list

print "Searching the list"
print my_list.index("database")

print "Deleting elements in the list"
my_list.remove("server")
print my_list

my_list = my_list + ["a","b","c"]
print my_list


