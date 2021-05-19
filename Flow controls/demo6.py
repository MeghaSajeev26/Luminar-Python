#percentage of classes
num1=int(input("enter number of classes held"))
num2=int(input("enter number of classes attended"))
percentage=(num2/num1)*100
if(percentage>=75):
    print("Allowed")
else:
    print("Not allowed")