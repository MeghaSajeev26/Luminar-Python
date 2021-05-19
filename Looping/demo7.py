#read limits and print only even numbers between the limits
lim1=int(input("enter lower limit"))
lim2=int(input("enter upper limit"))
while(lim1<=lim2):
    if(lim1%2==0):
        print(lim1)
    lim1+=1

