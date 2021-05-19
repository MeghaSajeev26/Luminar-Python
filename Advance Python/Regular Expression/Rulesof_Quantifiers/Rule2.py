import re
x="a*"   #count including zero number of a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print("Match at:",match.start())
    print("Group:",match.group())