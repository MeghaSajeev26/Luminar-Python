#constructors are used to initialize instance variables
#they automatically gets invoked when creating objects

class Person:
    def __init__(self,name,age,gender):  #__init__ is the constructor
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
per=Person("Anu",25,"Female")   #using constructors--'methods' can be called at the time of creating 'object'
per.printval()

