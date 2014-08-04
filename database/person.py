#/usr/bin/env Python

class Person:
	def __init__(self,name,age,salary=0,jobType='None'):
		self.name = name
		self.age = age
		self.salary = salary
		self.jobType = jobType
	def getDetails(self):
		print 'name	==>', self.name
		print 'age	==>', self.age
		print 'salary	==>', self.salary
		print 'jobType	==>', self.jobType
	def giveRaise(self,percent):
		self.salary = self.salary * (1.0+percent)






