import re
x="a+"  #a including group
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print("match at:",match.start())
    print("group:",match.group())