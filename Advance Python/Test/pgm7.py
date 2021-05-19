#7. Create a valid phone numbers file from the following file?
# +915678905432 +914567890321 765432167 123450987765 +919976532456

import re

r=open("ph_no","r")
f=open("Numbers","w")
x="[+][9][1]+\d{10}$"
for number in r:
    num=number.rstrip("\n")
    match = re.fullmatch(x,number)
    if match is not None:
        f.write(num)
        f.write("\n")