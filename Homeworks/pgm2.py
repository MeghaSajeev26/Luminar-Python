lst=[10,20,21,22,23]
lst2=[20,21,10,22,23]
# #check whether two list are same

for i in lst:
    if i in lst2:
        print("same")
        break
    else:
        print("not same")