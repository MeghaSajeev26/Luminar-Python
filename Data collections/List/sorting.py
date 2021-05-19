#sort a list in ascending order

list=[88,-96,888,4,33,6666]
print(list)

new_list=[]
while list:
     min=list[0]
     for i in list:
         if i<min:
             min=i
     new_list.append(min)
     list.remove(min)    #doesnt need to compare 'min' again

print(new_list)



#sorting using 'sort' keyword
#
# list.sort()
# print(list)
