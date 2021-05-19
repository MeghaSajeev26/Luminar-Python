#position of 'a' in the given group of number

import re
x="a{2}"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())