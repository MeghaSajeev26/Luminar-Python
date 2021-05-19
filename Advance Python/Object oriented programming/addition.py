#addition of two numbers using object oriented concept

class Addition:
    def details(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printval(self):
        print("Sum of numbers:",self.num1+self.num2)

obj=Addition()
obj.details(3,4)
obj.printval()