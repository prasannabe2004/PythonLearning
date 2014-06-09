class Employee():
    
    def __init__(self,firstName, lastName, employeeNum, age):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeNum = employeeNum
        self.age = age
        
    def getInfo(self):
        print(self.firstName+self.lastName+" "+str(self.employeeNum)+" "+str(self.age))
        
#class FullTime(Employee):
#   def __init__():
        
