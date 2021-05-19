# from packages import pgm1    #to import packages
# pgm1.add(2,4)
# pgm1.sub(7,6)

#to import from subdirectory---maindir_name.subdir_name


#using aliasing
# from packages import pgm1 as p
# p.add(2,4)
# p.sub(7,5)


#to call a single function
from packages.pgm1 import add
add(2,3)