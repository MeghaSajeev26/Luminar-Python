#Person class inheritence using constructors
class Person:
    def __init__(self,name,age):  #__init__ is the constructor
        self.name=name
        self.age=age
        print("Name:",self.name)
        print("Age:",self.age)
