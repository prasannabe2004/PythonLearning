# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    total = total + float(line[20:].rstrip())
    count = count + 1
avg = total/count
print ("Average spam confidence:", avg)
