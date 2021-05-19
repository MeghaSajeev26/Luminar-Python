#grade of subject marks
num1=int(input("enter sub1 mark"))
num2=int(input("enter sub2 mark"))
num3=int(input("enter sub3 mark"))
num4=int(input("enter sub4 mark"))
num5=num1+num2+num3+num4
if(num5>=180):
    print("A+")
elif(num5>=168)&(num5<=179):
    print("A")
elif(num5>=140)&(num5<=159):
    print("B+")
elif(num5>=120)&(num5<=139):
    print("B")
elif(num5>=100)&(num5<=119):
    print("C+")
elif(num5>=80)&(num5<=99):
    print("C")
elif(num5>=60)&(num5<=79):
    print("D+")
else:
    print("Fail")