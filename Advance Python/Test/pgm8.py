# When is the finally block executed.Explain with example?

#finally block is used in case of exception handling
#exception handling is used to handle diff. types of error
#One such error is ---index out of range--error
#when the index given by the user is out of the range specified,this error occurs.
#for exexution of this type ,we have two block --try and except (where only one block executes at a time)

list=[1,2,3,4]
a=int(input("enter index"))
try:
    print(list[a])
except:
    print("Exception occured")
finally:
    print("inside finally")   #but finally block executes all the time--
                                    # ie.,along with 'try' and 'except' blocks