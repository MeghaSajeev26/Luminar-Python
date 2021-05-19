#ending with 'a'----consider the whole string

import re
x="a$"
r="aaa abc aaaa cga"  #check string ending with 'a'
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())