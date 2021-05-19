l=[1,2,3,4,5]
print(l)
num=int(input("enter a number"))
def linear():
    for i in l:
        if num in l:
            print("number found")
        else:
            print("number not found")
        break
linear()
print()
