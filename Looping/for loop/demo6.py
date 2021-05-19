#check whether a number is prime or not

num=int(input("enter a number"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
if(flag>0):
    print(num,"is not a prime")
else:
    print(num,"is prime")