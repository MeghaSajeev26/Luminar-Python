#Rule 4-- A to Z

import re

x="[A-Z]" #A to Z
matcher=re.finditer(x,"AXV DFGJTNG")
for match in matcher:
    print(match.start())
    print(match.group())