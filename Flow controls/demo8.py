#place of service
age=int(input("enter your age"))
sex=input("enter your sex")
mar=input("enter your marital status")
if(sex=='F'):
    print("work only in urban areas")
elif(sex=='M')&(20>=age<=40):
    print("work anywhere")
elif(sex=='M')&(40>=age<=60):
    print("work only in urban areas")
else:
    print("ERROR")