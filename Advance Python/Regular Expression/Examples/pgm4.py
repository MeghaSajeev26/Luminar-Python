#starting with 'a' and ending with 'b'
import re
x="^a[a-zA-Z0-9\W]*b$"
n=input("Enter input")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")