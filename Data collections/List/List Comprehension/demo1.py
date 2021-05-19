#squares in list

# l=[1,2,3,4]
# l1=[]
# for i in l:
#     l1.append(i**2)
# print(l1)

#list comprehensions are used for creating new lists from other iterables
#as list comprehensions return lists, they consist of brackets containing the expression
#which is executed for each element along with the for loop to iterate over each element

l=[1,2,3,4]
squares=[n**2 for n in l]
print(squares)
