fname = input("Enter file name: ")
fh = open(fname)

list1 = []

for line in fh:
	lst = line.split()
	for i in lst:
		if i in list1:
			continue
		list1.append(i)

print(sorted(list1))
