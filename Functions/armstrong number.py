#153=1*1*1 + 5*5*5 + 3*3*3  //153 is an armstrong number

num=int(input("enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    temp//=10
    sum += digit ** 3
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")