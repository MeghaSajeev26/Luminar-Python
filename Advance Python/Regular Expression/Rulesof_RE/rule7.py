#rule 7--check special symbols

import re

x="[^a-zA-Z0-9]" #a to z
matcher=re.finditer(x,"Acv @#4%&Fes)")
for match in matcher:
    print(match.start())
    print(match.group())