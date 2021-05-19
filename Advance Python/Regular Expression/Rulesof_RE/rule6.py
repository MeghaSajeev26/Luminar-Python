#rule 6--- check digits

import re

x="[0-9]" #from 0 to 9
matcher=re.finditer(x,"120 4902848")
for match in matcher:
    print("Match at:",match.start())
    print("Group:",match.group())