#!/usr/bin/python

my_dict = {"server":"mpilgrim", "database":"master"}

print my_dict
# Accessing the dictionary
print my_dict["server"], my_dict["database"]

#Modifying the dictionary
my_dict["server"] = "computer"

print my_dict

#Adding element to dictionary
my_dict["uid"] = "sa"

#Add duplicate
my_dict["uid"] = "sa"

print my_dict # Duplicate is not found

my_dict["prasanna"] = "genious"

print my_dict

#Case sensitive
my_dict["Prasanna"] = "genious"

print my_dict

#Delete a key from Dictionary

del my_dict["prasanna"]

print my_dict