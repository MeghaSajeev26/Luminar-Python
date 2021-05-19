#opposite triangle

def pattern(n):
    for i in range(0,n):
        for j in range(i,n):
            print("*",end=' ')
        print("\r")
pattern(6)