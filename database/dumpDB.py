import shelve

db = shelve.open('class-shelve')

for key in db:
	i = db[key]
	i.getDetails()
	i.giveRaise(0.1)
	i.getDetails()

db.close()

	
