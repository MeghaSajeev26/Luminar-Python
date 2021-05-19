#rule 5---a-zA-Z

import re

x="[a-zA-Z]" #lower and upper a to Z
matcher=re.finditer(x,"aAXVv DFGsJfTgNG")
for match in matcher:
    print(match.start())
    print(match.group())