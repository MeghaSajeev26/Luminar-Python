#Hierarchial/Multilevel inheritence
class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print("Name:",self.name)
        print("Age:",self.age)
class Job(Person):
    def detail(self,designation,location):
        self.designation=designation
        self.location=location
        print("Job:",self.designation)
        print("Locality:",self.location)
class Vehicle(Job):
    def print(self):
        print("I have a car")
per=Vehicle()
per.details("Akhil",25)
per.detail("Manager","Kakkanad")
per.print()