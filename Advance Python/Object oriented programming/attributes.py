#defining attributes inside Class

class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
obj=Person()
obj.details("anu",22)
obj.printval()