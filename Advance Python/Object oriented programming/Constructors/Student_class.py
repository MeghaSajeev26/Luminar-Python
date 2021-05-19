#student class using constructors
class Student():
    School="St.therese"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("Name of Student:",self.name)
        print("Age:",self.age)
        print("School:",Student.School)
st=Student("Akash",16)
st1=Student("Ramya",16)
st.printval()
st1.printval()