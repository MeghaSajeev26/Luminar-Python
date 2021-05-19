def revert_value(fun):
    def wrapper(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return fun(num1,num2)
    return wrapper

@revert_value
def div(num1,num2):
    return num1/num2

@revert_value
def sub(num1,num2):
    return num1-num2

print(div(2,8))
print(sub(7,8))
