#Rule for phone number validation
import re
x="[+][9][1]+\d{10}"
n=input("Enter number")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")