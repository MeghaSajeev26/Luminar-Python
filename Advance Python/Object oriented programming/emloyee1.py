#employee account using class variable
class Employee():
    company="Global Services"
    def details(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    def printval(self):
        print("Name:",self.name)
        print("Employee id:",self.emp_id)
        print("Company name:",Employee.company)
obj=Employee()
obj.details("Abhi",101)
obj.printval()
print("\r")
obj1=Employee()
obj1.details("Rakesh",102)
obj1.printval()