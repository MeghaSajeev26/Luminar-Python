#Person,Student,Parent,Child
#Person-->Child
#Person-->Parent
#Child-->Student
class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print("Name:",self.name)
        print("Age:",self.age)
class Parent(Person):
    def de(self,location):
        self.location=location
        print("Location:",self.location)
class Child(Person):
    def printval(self):
        print("He owns a car")
class Student(Child):
    def account(self,student_id):
        self.student_id=student_id
        print("id:",self.student_id)
per=Parent()
per.details("Akash",22)
per.de("Kerala")
print("\r")
ch=Student()
ch.details("Akhil",25)
ch.printval()
ch.account(101)