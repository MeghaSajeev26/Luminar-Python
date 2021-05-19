#1.break
#1 to 50
# for i in range(1,51):
#     if(i==25):
#         break
#     print(i)
#to exit from a loop when a condition satisfies--break is used


#2.continue
#1 to 24....26 to 50
# for i in range(1,51):
#     if(i==25):
#         continue
#     print(i)
#continue--used to skip a given condition and the control is given back to the loop


#3.pass---do nothing

num=int(input("enter number"))
if(num%2==0):
    print(num)
else:
    pass  #DO NOTHING
