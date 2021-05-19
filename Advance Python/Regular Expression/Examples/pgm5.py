#minimun length 8--maximum length 15--except numbers
import re
x="\D{8,15}$"   #'$' symbol can be also used to specify the end of a rule
n=input("Enter input")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")

