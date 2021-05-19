#types of tuples

#1.Empty tuple
mytuple=()
print(mytuple)

#2.Integer tuple
mytuple1=(1,2,3)
print(mytuple1)

#3.Tuple with different datatypes
mytuple2=(1,"megha",4.5)
print(mytuple2)

#4.Nested tuple
mytuple4=(1,2,[1,3],("megha"))
print(mytuple4)

#5.Tuple with one element---should always be seperated using comma
#otherwise it will be read as an 'int' or a 'string'
mytuple5=3,
print(mytuple5)
print(type(mytuple5))