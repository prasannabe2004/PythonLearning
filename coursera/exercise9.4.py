name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mydict = {}

for line in handle:
    if line.startswith('From '):
        sender = (line.split()[1])
        if sender in mydict:
            mydict[sender] = mydict[sender] + 1
        else:
            mydict[sender] = 1

maxvalue = None
maxkey = None
for key,val in mydict.items():
    if maxvalue == None:
        maxvalue = val
    if maxvalue < val:
        maxvalue = val
        maxkey = key

print (maxkey,maxvalue)
