# variable length argument method
#------used to ease the method of calling many arguments
#
# addThree ---camlin notation
# add_three --- snake notation

# def add(*args):  #args=(10,20)    #*--tuple accessing
#     res=0
#     for num in args:    #10
#         res+=num   #res=0+10=10+20=30+30=60
#     return res  #60
# print(add(10,20,30))  #accepts any number of arguments in 'tuple' format


# def print_employee(**kwargs):  #** --- key value pair --dictionary format
#     print(kwargs)
# print_employee(id=100,name="ajay",salary=10000)

#(OR)

# def print_employee(**kwargs):
#     for k,v in kwargs.items():
#         print(k,">=",v)
# print_employee(id=100,place="pkd",job="ekm")


# arr=[2,44,55,11,4,89]
# arr.sort()  #to sort a given array
arr.sort(reverse=True) #to sort an array in the reverse order
#obj.method format --- arr is the object ----sort is the method
# print(arr)

#Another method for sorting
# arr=[2,44,55,11,4,89]
srt=sorted(arr,reverse=True) #to sort an array in the reverse order
#srt -- is the funtion
# print(srt)


# * args --tuple
# **kwargs --dictionary
#both accepts any number of arguments, including 0 no.og args
#arr---accepted by *args
#reverse=True ---is accepted by '**kwargs'










