#print employee with salary above 15k

list=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000)]
salary=0
for i in list:
    if(i[3]>15000):
        print(i)
