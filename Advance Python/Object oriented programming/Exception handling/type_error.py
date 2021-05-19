#data type error


try:
    a = int(input("enter num1"))    #given inside try---because error occurs while giving input
    b = int(input("enter num2"))
    print(a+b)
except:
    print("entered value is not an integer")   #all blocks executes at the same time in this case
finally:
    print("finally")

