#Regular Expression--Pattern matching

#R.E--package for pattern matching

import re  #importing the package-R.E
count=0 #used for finding the count of expression
matcher=re.finditer('ab','abaabbab')  #finditer is the method used for iteration
#(to find the count of 'ab' in the given expression)
for match in matcher:  #'match' and 'matcher' are variables
    count+=1
print("Count=",count)
