l=[1,2,3,4,5,33,-1,0]

def binary():
    l.sort()
    print(l)
    ele=int(input("enter a number"))
    flag=0
    low=0
    upper=len(l)-1

    while low<=upper:
        mid=(low+upper)//2

        if ele>l[mid]:
            low=mid+1
        elif ele<l[mid]:
            upper=mid-1
        elif ele==l[mid]:
            flag=1
            break
    if flag==1:
        print("found")
    else:
        print("not found")

binary()