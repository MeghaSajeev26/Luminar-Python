#6. Create objects of the following file and print the details of student with maximum mark?
#anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,bca,198 maya,5, bba,195

class Details:
    def __init__(self,name,rollno,dept,mark):
        self.name=name
        self.rollno=rollno
        self.dept=dept
        self.mark=mark
    def printval(self):
        print("Name:",self.name)
        print("Roll number:",self.rollno)
        print("Department:",self.dept)
        print("Marks obtained:",self.mark)
    def __str__(self):
        return self.name

f=open("student","r")
lst = []
for line in f:
    data=line.rstrip("\n").split(",")
    name=data[0]
    rollno=data[1]
    dept=data[2]
    mark=int(data[3])
    obj=Details(name,rollno,dept,mark)
    lst.append(obj)

mark=[]
for st in lst:
    mark.append(st.mark)
print(mark)
for st in lst:
    if(st.mark==max(mark)):
        print("Details of student with maximum mark:",st.rollno,st.name,st.dept,st.mark)



