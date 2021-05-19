#List Comprehension
employees = [
    {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 28000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
]
#Name of employees
# e_names=[emp["name"] for emp in employees]  #emp--one set of employee object
# print("Name of employees:",e_names)    #emp["name"]---returning name from the employee object

#Employee names in Upper case
# u_names=[emp["name"].upper() for emp in employees]  #emp--one set of employee object
# print("Name of employees in Caps:",u_names)

#Employee names starting with 'a'
# a_names=[emp["name"] for emp in employees if emp["name"][0]=='a']  #emp--one set of employee object
# print("Name of employees starting with 'a':",a_names)

#Employees with salary above 23000
salary=[emp for emp in employees if emp["salary"]>23000]
print(salary)
