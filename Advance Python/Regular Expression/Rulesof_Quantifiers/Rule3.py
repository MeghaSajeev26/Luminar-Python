#checking as individual,doesn't consider 'a' as a group

import re
x="a?"  #count a as each including zero number of a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print("Match at:",match.start())
    print("Element:",match.group())