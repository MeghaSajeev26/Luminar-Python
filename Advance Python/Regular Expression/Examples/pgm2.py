#Rule for '56kg'

import re
x="\d{2}[a-z]{2}"   #{2}--checking 2 digits and 2 alphabets together
n="56kg"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")