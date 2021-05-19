#year month date--read
#dob year,age,date--read
#to print--your age
d1=int(input("enter ur day of birth"))
m1=int(input("enter ur month of birth"))
y1=int(input("enter ur year of birth"))
print("date of birth is",d1,"/",m1,"/",y1)
d2=int(input("enter today's day"))
m2=int(input("enter this month"))
y2=int(input("enter this year"))
if(m1>m2):
    m=m2+(12-m1)
else:
    m=m2-m1
if(m1>m2):
    y=y2-y1-1
else:
    y=y2-y1
if(d2>d1):
    d=d2-d1
else:
    d=d1-d2
print("you are",y,"years",m,"months",d,"days old")