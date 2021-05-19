#rule to validate vehicle registration number
import re
x="[K][L]\d{2}[A-Z]{2}\d{4}"
n=input("Enter input")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")