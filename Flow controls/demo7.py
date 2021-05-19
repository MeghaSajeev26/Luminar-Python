#net bonus
salary=int(input("Enter salary"))
service=int(input("Enter years of service"))
if(service>5):
    print("Bonus awarded=",(salary)*5/100)
else:
    print("Not eligible for bonus")