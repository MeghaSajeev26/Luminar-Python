#starting with 'a'---consider the whole string

import re
x="^a"   #check string starting with a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())