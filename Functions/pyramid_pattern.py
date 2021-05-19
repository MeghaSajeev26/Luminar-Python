#pyramid pattern
def triangle(n):   #n=5
    k=2 * n-2   #k=2*5-2=8
    for i in range(0,n):   #(0,5)
        for j in range(0,k):   #0,8
            print(end=' ')
        k=k-1 #8=8-1=7
        for j in range(0,i+1):
            print("*",end=' ')
        print("\r")
triangle(9)