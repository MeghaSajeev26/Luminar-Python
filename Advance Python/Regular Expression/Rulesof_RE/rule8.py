#Rule 6--check space
import re

x="\s" #check space
matcher=re.finditer(x,"AdXV DghF GJTNG")
for match in matcher:
    print(match.start())
    print(match.group())