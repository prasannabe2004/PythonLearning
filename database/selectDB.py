import shelve

fieldnames = ('name','age','salary','jobType')

db = shelve.open('class-shelve')

while True:
	key = raw_input("\nKey->")
	if not key: break
	try:
		record = db[key]
	except:
		print 'No suck key ',key
	else:
		for field in fieldnames:
			print getattr(record, field)

db.close()

