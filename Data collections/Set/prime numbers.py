#set of prime numbers
s1={1,2,3,4,5,6,7,8,9,10}
prime=set()
nonprime=set()
for i in s1:
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                nonprime.add(i)
            else:
                prime.add(i)
print("prime numbers",prime)
print("Non prime numbers",nonprime)