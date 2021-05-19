#rule to validate email-id
import re
x="[a-zA-Z0-9_.+-]+[@][a-zA-Z0-9]+[.][c][o][m]$"   #\. -- to specify 'dot'
n=input("Enter input")            #(or) "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")