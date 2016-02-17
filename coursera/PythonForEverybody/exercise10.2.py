name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mydict = {}

for line in handle:
    if line.startswith('From '):
        time = (line.split()[5])
        hr = time.split(':')[0]
        if hr in mydict:
            mydict[hr] = mydict[hr] + 1
        else:
            mydict[hr] = 1

for h,c in sorted(mydict.items()):
    print(h,c)
