# n1=int(input("enter first number"))
# n2=int(input("enter second number"))
# print(n1/n2)

#Exception Handling
#Zero division error

n1=int(input("enter number1"))
n2=int(input("enter number2"))
try:
    print(n1/n2)
except:
    print("exception occured")  #only one block executes at a time

