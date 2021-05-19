#subtraction
# def sub(num1,num2):
#     if num1<num2:
#         (num1,num2)=(num2,num1)  ---feature
#     return num1-num2
# res=sub(30,20)
# print(res)

#decorators are used add a new feature to an existing function without changing the definition
#add the above feature to the function 'def sub' without making changes to the function
def dec_sub(fun): #a decorator fn always accepts an argument which is a 'function'
    def wrapper(num1,num2): #wrapper----the inner function inside a decorator function
        if num1<num2:
            (num1,num2)=(num2,num1)
        return fun(num1,num2)
    return wrapper

@dec_sub         #---dec_sub is the decorator function
def sub(num1,num2): #---def sub is the function to be decorated--since it has 2 arguments--decorator fn also have
    return num1-num2                                 #two number of arguments
res=sub(10,5)
print(res)

# def div(num1,num2):
#     return num1/num2
# res=div(2,30)
# print(res)



