#if num>5 ---num+1---else num-1
lst=[7,8,9,4,2]
p=[num+1 if num>5 else num-1 for num in lst]
print(p)