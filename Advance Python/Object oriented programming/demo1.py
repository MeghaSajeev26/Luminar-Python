#class : design pattern
#object : real world entity
#references : name that refers the memory location of an object

class Person:
    def walk(self):        #self is an instance variable related to methods(under a Class)
        print("person is walking")
    def jump(self):
        print("person is jumping")   #class : Person

obj=Person()   #obj--reference
obj.walk()
obj.jump()

obj2=Person()   #using different reference, many objects can be created
obj2.walk()
obj2.jump()