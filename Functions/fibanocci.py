#fibanocci series
#0
#1   0+1=1
#1
#2 1+1=2
#3
#5 2+3=5
#8 5+3=8

num=int(input("enter the number"))
n1=0
n2=1
count=0
while(count<num):   #0<5
    print(n1)   #0
    n3=n1+n2    #n3=0+1=1
    n1=n2     #0=1
    n2=n3   #1=1
    count+=1
