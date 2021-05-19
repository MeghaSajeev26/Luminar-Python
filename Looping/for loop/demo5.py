#sum of even and odd numbers within a given limit
low=int(input("enter lower limit"))
up=int(input("enter upper limit"))
sum=0
sum1=0
for i in range(low,up+1):
    if(i%2==0):
        sum=sum+i

    else:
        sum1=sum1+i

print("sum of odd numbers",sum1)
print("sum of even numbers",sum)