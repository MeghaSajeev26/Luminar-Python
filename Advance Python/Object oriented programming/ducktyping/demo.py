#duck typing-- Dynamic typing
#gives importance to the functionality ,more than the class
class Swift:
    def start(self):
        print("Swift car starts")
    def accelerate(self):
        print("Swift car acccelerates")
    def breaks(self):
        print("Swift car break method")
    def stop(self):
        print("Swift car stoppping method")

class Seltos:
    def start(self):
        print("Seltos car starts")
    def accelerate(self):
        print("Seltos car acccelerates")
    def breaks(self):
        print("Seltos car break method")
    def stop(self):
        print("Seltos car stoppping method")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.breaks()
        car.stop()
p=Person()              #gives importance to the four different functionalities --- start, accelerate
sw=Swift()                                   #breaks, and stop --- more than the two class -- Swift and Seltos
p.drive(sw)

#OR
# p=Person()
# sel=Seltos()
# p.drive(sel)