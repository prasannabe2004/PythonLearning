largest = None
smallest = None

while True:
    try:
        num_raw = input("Enter a number: ")

        if num_raw == "done" : 
            break
        num = int(num_raw)
        if largest == None:
        	largest = num
        if smallest == None:
        	smallest = num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num         
    except:
        print ('Invalid input')

print ("Maximum is", largest)
print ("Minimum is", smallest)
