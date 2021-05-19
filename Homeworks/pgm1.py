# if num>5 --num+1
# else num-1

# [8,9,10,3,2,0]

lst=[7,8,9,4,3,1]
# lst1=[]
# num=0
# for num in lst:
#     if num>5:
#         lst1.append(num+1)
#     else:
#         lst1.append(num-1)
# print(lst1)

#other method--- TERNARY OPERATOR
# lst2=[]
# for num in lst:
#     lst2.append(num+1) if num>5 else lst2.append(num-1)
# print(lst2)

#funtional pgming  ---map
# list3=list(map(lambda num:num+1 if num>5 else num-1,lst))
# print(list3)

#even numbers----filter
# evens=list(filter(lambda num:num%2==0,lst))
# print(evens)

#name starting with a--- filter
lsst=["megha","akhil","binu","chinnu","ajay"]
anames=list(filter(lambda name:name[0]=='a',lsst))
print(anames)




