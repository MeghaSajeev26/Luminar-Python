#*
#* *
#* * *
#* * * *
#* * * * *


#1
#2 2


#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5

#0 1 2 3 4 5
#0 1 2 3 4
#0 1 2 3
#0 1 2
#0 1
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=' ')
#     print()




#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1

for i in range(0,5): #0  1
    for j in range(i+1,0,-1):  #(1,0)   (2,0)
        print(j,end=' ') #1 #2 1
    print()