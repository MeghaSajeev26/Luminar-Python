# 9. Write a Python program to find the sequences of
# one upper case letter followed by lower case letters?

import re
x="[A-Z][a-z]*"
n=input("Enter sequence")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")