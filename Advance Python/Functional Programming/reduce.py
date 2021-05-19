#single output---reduce
#2 paramerters are passed

# import functools  #reduce is imported from 'functools' module
# arr=[1,2,3,4,5,6]
# total=functools.reduce(lambda num1,num2:num1+num2,arr)
# print(total)

# from functools import*    #to avoid specifying 'functools.reduce' everytime
# highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,arr)
# print(highest)

#in reduce--only numbers can be passed---min,mix,sum,highest etc can be used to reduced into a single value

#print highest salary
from functools import reduce
employees = [
    {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 28000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]
high_sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                list(map(lambda emp:emp["salary"],employees))) #for considering only salaries
print(high_sal)