#Rule 3--a to z

import re

x="[a-z]" #a to z
matcher=re.finditer(x,"abt cSwfghf")
for match in matcher:
    print(match.start())
    print(match.group())