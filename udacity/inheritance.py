class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("last name ="+self.last_name)
        print("Eye color ="+self.eye_color)
        
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print ("Child constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        print("last name ="+self.last_name)
        print("Eye color ="+self.eye_color)
        print("Toys ="+str(self.number_of_toys))
        
billy_cyrus = Parent("cyrus","blue")
#print(billy_cyrus.last_name)
#billy_cyrus.show_info()

miley_cyrus = Child("Cyrus","Blue",10)
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()
