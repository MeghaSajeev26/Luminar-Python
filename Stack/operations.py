#stack operations using list

stack=[]
size=int(input("enter the size"))
top=0

n=0
def push():
    global top,size
    if(top>size):
        print("stack is full")
    else:
        p=int(input("enter the element"))
        stack.append(p)
        top+=1

def pop():
    global top,size
    if(top<=0):
        print("stack is empty")
    else:
        o=int(input("enter the element"))
        stack.pop()
        top-=1

def display():
    print(stack)

while(n!=1):
    print("enter the operation")
    operation=int(input("1.Pop  2.Pop  3.Display"))
    if(operation==1):
        push()
    elif(operation==2):
        pop()
    elif(operation==3):
        display()

    n=int(input("do you want to continue? Press 1 for exit"))
