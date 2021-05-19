# 10. Write a Python program that matches
# a string that has an 'a' followed by anything, ending in 'b'?

import re
x="(^a[a-zA-Z0-9\W]*b$)"
# x="[a][a-zA-Z0-9\W]*[b]"
n=input("Enter sequence")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")