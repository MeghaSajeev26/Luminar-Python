#index out of range--error
#when the index given by the user is out of the range specified,this error occurs.

list=[1,2,3,4]
a=int(input("enter index"))
try:
    print(list[a])
except:
    print("Exception occured")
finally:
    print("inside finally")   #executes all the time--ie.,along with 'try' and 'except'