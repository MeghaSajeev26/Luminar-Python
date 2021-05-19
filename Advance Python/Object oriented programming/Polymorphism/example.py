#method overriding
class Vehicle:
    def veh_mod(self):
        print("vehicle is a car")
    def show(self):
        print("Vehicle has 10lks")
class Model(Vehicle):
    def veh_mod(self):
        print("Vehicle is a bus")
m=Model()
m.veh_mod()  #'Vehicle' class method is overridded by 'Model' class method