#eg for multiple inheritence
class Company:
    def details(self,name,place):
        self.name=name
        self.place=place
        print("Company name:",self.name)
        print("Located in:",self.place)
class Id:
    def printval(self):
        print("I have employee id")
class Employee(Company,Id):
    def account(self,name,gender,dept):
        self.name=name
        self.gender=gender
        self.dept=dept
        print("Name of employee:",self.name)
        print("Gender:",self.gender)
        print("Department:",self.dept)
co=Company()
co.details("Regal Associates","Ernakulam")
ab=Id()
ab.printval()
print("\r")
em=Employee()
em.details("Global Services","Palakkad")
em.account("Akash","Male","Accounts")
em.printval()