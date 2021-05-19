#Person class without using constructor including inheritence
#Single inheritence--deriving a child  class from a parent class
class Person():
    def detail(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):  #'Student' is the subclass derived from superclass-'Person'
    def print(self,dept,college):     #superclass/base class/parent
        self.dept=dept                 #derived class/subclass/child class
        self.college=college
        print(self.dept)
        print(self.college)
per=Person()
per.detail("Anu",22,"Female")
st=Student()
st.print("CS","St.Xavier")
print('\r')
st.detail("Anand",24,"Male")
