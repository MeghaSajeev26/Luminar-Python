#combination of upper case and lower case numbers ending with a number
import re
x="[a-zA-Z]+\d$"   #or  "[a-zA-Z]+[0-9]$"
n=input("Enter input")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")