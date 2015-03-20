def computepay(h,r):
    if h <= 40:
        return h * r
    else:
    	return (40 * r) + ((h -40) * r * 1.5)

hrs = input("Enter Hours:")
hours = float(hrs)
rte = input("Enter rate:")
rate = float(rte)
    
    
p = computepay(hours,rate)

print (p)
