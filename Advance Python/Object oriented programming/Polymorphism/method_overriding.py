class Parent:
    def properties(self):
        print("10 lkhs ")
    def marry(self):
        print("with ram")
class Child(Parent):
    def marry(self):
        print("with arun")

c=Child()
c.marry()  #when two classes(Parent and Child) have same methods,parent class method will be overridded
                                 #                                              by child class method
                                 #here 'marry' is the method