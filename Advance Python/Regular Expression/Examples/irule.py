import re
x="\w*"
n="hellooo"
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")