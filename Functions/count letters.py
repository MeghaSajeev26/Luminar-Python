a=input("enter str")
b=input("enter element count")
count=0
for i in a:
    if i in b:
        count+=1
print("count is",count)