# print employee names only map()
#print all employee name into uppercase  map()
#print employe deatails whose name starting with 'a'   ==a  filter()


#print employee details whode salary > 23000  filter()

#print employee details whose designation==developer
employees = [
    {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]

# e_names=list(map(lambda emp:emp["name"],employees))
# print(e_names)
# upnames=list(map(lambda name:name.upper(),e_names))
# print(upnames)
# a_names=list(filter(lambda emp:emp["name"][0]=='a',employees))
# print(a_names)
# sal=list(filter(lambda emp:emp["salary"]>23000,employees))
# print(sal)
# developers=list(filter(lambda emp:emp["designation"]=="developer" and emp["salary"]>24000,employees))
# print(developers)
