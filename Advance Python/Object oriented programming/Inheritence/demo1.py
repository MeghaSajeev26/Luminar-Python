#Multiple Inheritence
#2 parent class for a single child class

class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Mobile:
    def printval(self):
        print("I have 1+")
class Child(Person,Mobile):
    def info(self,college,place):
        self.college=college
        self.place=place
        print(self.college)
        print(self.place)
per=Person()
per.details("Anu",22)
mob=Mobile()
mob.printval()
ch=Child()
ch.details("Amal",23)
ch.printval()
ch.info("St.thomas College","Kerala")
