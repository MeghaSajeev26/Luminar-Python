#find number of students with pass from total
totalstudents=("anu","jiya","amal","adhul","nandu","aiswarya")
failed=("jiya","amal","nandu")
passed=set()
for i in totalstudents:
     if i not in failed:
        passed.add(i)
print("passed students are",passed)
