class Work:
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

f=open("work","r")
lst = []
for line in f:
    data=line.rstrip("\n").split(",")
    name=data[0]
    rollno=data[1]
    dept=data[2]
    mark=int(data[3])
    obj=Work(name,rollno,dept,mark)

    # print(obj)
    # obj.printval()

#to print no.of students with mark > 190

    lst.append(obj)
for i in lst:
    if i.mark>190:
        print(i)
