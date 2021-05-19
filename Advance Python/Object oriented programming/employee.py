#create employee class with attributes--name,age,empid,salary,department,company

class Employee:
    def details(self,name,age,emp_id,salary,dept,company):
        self.name=name
        self.age=age
        self.emp_id=emp_id
        self.salary=salary
        self.dept=dept
        self.company=company
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.emp_id)
        print(self.salary)
        print(self.dept)
        print(self.company)
obj=Employee()
obj.details("Rakesh",28,401,25000,"Accounts","Global Services")
obj.printval()