hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

if h <= 40:
    print (h * r * 1)
else:
    print (h * r * 1  + (h-40)*r * 1.5)
