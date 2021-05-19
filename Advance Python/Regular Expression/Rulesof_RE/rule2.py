#Rule 2--except a,b and c

import re

x="[^abc]"  #except a,b or c
matcher=re.finditer(x,"abt cQsfgh")
for match in matcher:
    print(match.start())
    print(match.group())