import re

x = 'My 2 favorite numbers are 9 and 42'

y = re.findall('[0-9]+', x)

print(y)

x = 'From prasannabe2004@gmail.com Sat Jun 5 09:14:16 2016'

y = re.findall('\S+@\S+', x)

print(y)

x = 'From   prasannabe2004@gmail.com Sat Jun 5 09:14:16 2016'

y = re.findall('^From   (\S+@?\S+)', x)

print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

y = re.findall('[0-9a-z]',x)

print(y)


x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y