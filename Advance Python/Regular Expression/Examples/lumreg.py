#copy only the python register numbers

import re
r=open("lumregno","r")
f=open("PythonReg","w")
x="[L][U][M]\d{2}[P][Y]\d{3}$"
for i in r:
    regnum=i.rstrip("\n")
    # print(i)
    match = re.fullmatch(x,regnum)
    if match is not None:
        f.write(i)
        f.write("\n")