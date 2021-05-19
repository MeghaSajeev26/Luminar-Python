#position and group of match in expressions

import re
count=0
matcher=re.finditer('ab','abaabbab')
for match in matcher:
    print("Match available at:",match.start()) #to get the position of match
    print("Group:",match.group()) #group of the match(ie,'ab')
    count+=1
print("Count=",count)