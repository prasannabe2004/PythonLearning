import shelve
from person import Person
from manager import Manager

def main():
	bob = Person("Bob Smith",42, 40000,'software')
	sue = Person("Sue Jones",45, 45000,'hardware')
	tom = Manager("Tom Doe", 50, 50000)
	
	db = shelve.open('class-shelve')

	db['bob'] = bob
	db['sue'] = sue
	db['tom'] = tom

	name = db['bob']
	name.getDetails()

	db.close()

if __name__ == '__main__':
	main()
