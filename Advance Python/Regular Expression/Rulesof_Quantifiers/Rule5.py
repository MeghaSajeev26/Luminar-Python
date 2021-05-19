#min and max group of 'a'

import re
x="a{2,3}"  #min 2 a and max 3 a
r="aaa abc aaaa aa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print("match at:",match.start())
    print("Group :",match.group())