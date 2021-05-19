#4. Create an Animal class using constructor and build a child class 'Dog' for Animal?
class Animal:
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour
    def printval(self):
        print("Breed:",self.breed)
        print("Colour:",self.colour)
class Dog(Animal):
    def __init__(self,name,age,breed,colour):
        super().__init__(breed,colour)
        self.name=name
        self.age=age
    def print(self):
        print("Name:",self.name)
        print("Age:",self.age)
dg=Dog("Shadow",3,"German Shepherd","Coffee Brown")
dg.printval()
dg.print()
