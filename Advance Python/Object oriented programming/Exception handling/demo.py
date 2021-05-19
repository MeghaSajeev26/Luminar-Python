#exception handling
num1=int(input("enter num1"))
num2=int(input("enter num2"))
try:
    result=num1/num2
    print(result)
except:
    print("Exception occured")
# except Exception as e: ---Exception is the class--- 'as e' is given to specify aliasing
    # print("exception occured",e.args)   ---'e.args'-- to display the type of exception occured


#types of exceptions---
#div by 0
#index out of range
#file not found
#type error         ----all these errors are included in a class called 'Exception' which catches the mentioned
                                                      #errors when they occur