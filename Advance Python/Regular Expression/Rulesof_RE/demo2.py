#Rules for validation of R.E

#Rule--either a,b or c

import re

x="[abc]"  #search either a,b or c
matcher=re.finditer(x,"abt cQsfgh")
for match in matcher:
    print(match.start())
    print(match.group())