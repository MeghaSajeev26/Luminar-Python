#5!=5*4*3*2*1

n=int(input("enter the number:"))
factorial=1
if(n<0):
    print("sorry factorial doesnt exist for negative numbers")
elif(n==0):
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print("factorial of",n,"is",factorial)