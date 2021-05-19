#1. Create a child class Bus that will inherit all of the variables and
#methods of Vehicle class?

class Vehicle:
    def details(self,no,model,colour):
        self.no=no
        self.model=model
        self.colour=colour
        print("Vehicle Number:",self.no)
        print("Vehicle Model:",self.model)
        print("Vehicle Colour:",self.colour)
class Bus(Vehicle):
    def print(self,reg):
        self.reg=reg
        print("Vehicle Registration:",self.reg)
ch=Bus()
ch.details("KL52MK3345","2019","Blue")
ch.print("Kerala")
