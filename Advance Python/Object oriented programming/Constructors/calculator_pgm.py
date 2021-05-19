#Calculator program using constructor
class Calculator():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("Number1=",self.x)
        print("Number2=",self.y)
    def add(self):
        print("add=",self.x+self.y)
    def sub(self):
        print("sub=",self.x-self.y)
    def mul(self):
        print("mul=",self.x*self.y)
    def div(self):
        print("div=",self.x/self.y)
cl=Calculator(9,3)
cl.add()
cl.sub()
cl.mul()
cl.div()