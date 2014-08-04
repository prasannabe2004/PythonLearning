from person import Person

class Manager(Person):
	def __init__(self,name,age,salary):
		Person.__init__(self,name,age,salary,'manager')
	def giveRaise(self, percent,bonus=0.1):
		Person.giveRaise(self,percent+bonus)
