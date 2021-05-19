initial=int(input("enter initial range"))
final=int(input("enter final range"))
for i in range(initial,final):
        if(i%2==0):
            r=6
            for k in range(r,0,-1):
                for j in range(0,k):
                    print(i,end=' ')
                print("\r")
        else:
            r2=6
            for l in range(r2):
                for m in range(0,l+1):
                    print(i,end=' ')
                print("\r")