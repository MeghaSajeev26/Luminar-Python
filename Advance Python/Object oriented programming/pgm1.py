#class variable is used to define common element within a Class
class Student:
    college="St.Xavier"  #class variable(common among a Class)
    def details(self,name,s_id):
        self.name=name    #self is an instance variable related to methods(under a Class)
        self.s_id=s_id
    def printval(self):
        print("Name of Student:",self.name)
        print("Student id:",self.s_id)
        print("College:",Student.college) #college is a class variable
obj=Student()
obj.details("Anu",101)
obj.printval()
print("\r")
obj1=Student()
obj1.details("Amal",102)
obj1.printval()