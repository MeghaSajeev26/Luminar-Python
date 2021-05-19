#create a function print_employee() => calling fn print_employee(id=1000) , prop=salary, prop=designatn
# it will return name of that employee

employees={
    1000: {"eid": 1000, "name": "ajay", "salary": 25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun","salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
}

def print_employee(**kwargs):  #kwargs={id:1000,prop:salary}
    id=kwargs["id"]  #1000
    prop=kwargs["prop"] #salary

    if id in employees:
        print(employees[id]["name"]) #employees[1000]
        print(employees[id][prop])   #employees[1000]
    else:
        print("Invalid ID")
print_employee(id=1002,prop="salary")