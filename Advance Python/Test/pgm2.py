#Create an example for three types of inheritance in one
# program by using Person as main class?
class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print("Name:",self.name)
        print("Age:",self.age)
class Teacher(Person):
    def dep(self,dept):
        self.dept=dept
        print("Subject:",self.dept)
class Col(Teacher):
    def co(self,coll):
        self.coll=coll
        print("College:",self.coll)
class Subject():
    def sub(self,subject):
        self.subject=subject
        print("Subject:",self.subject)
class Student(Col,Subject):
    def st(self,gender,place):
        self.gender=gender
        self.place=place
        print("Gender:",self.gender)
        print("Place:",self.place)
#single level
per=Teacher()
per.details("Akhil",23)
per.dep("Science")
print('\r')
#muti level
cl=Col()
cl.details("Akshay",23)
cl.dep("Commerce")
cl.co("St.xavier")
print('\r')
#multiple
stu=Student()
stu.details("Rahul",23)
stu.co("St.xavier")
stu.dep("Science")
stu.st("Male","Kerala")