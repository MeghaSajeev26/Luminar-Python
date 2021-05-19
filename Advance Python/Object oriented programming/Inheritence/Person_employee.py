#person -employee class using  single inheritence
class Person():
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
class Employee(Person):
    def print(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
        print("Employee id:",self.emp_id)
        print("Salary:",self.salary)
per=Person()
per.details("Amal",22,"Male")
print('\r')
emp=Employee()
emp.print(1001,25000)
emp.details("rakesh",26,"Male")

