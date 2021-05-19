#check whether the user input key is present or not

dict={'name':"megha",'age':22,'place':"palakkad"}
# a=input("type key here")
# for i in dict:
#     if i==a:
#         print("present")
#         break
# else:
#     print("not present")


#using function

def is_present(x):
    if x in dict:
        print("present")
    else:
        print("not present")
is_present("megha")
is_present('name')