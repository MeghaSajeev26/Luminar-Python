class Pycharm:
    def compile(self):
        print("Complie using pycharm")
    def execute(self):
        print("Execute using pycharm")

class Vscode:
    def compile(self):
        print("Complie using vscode")
    def execute(self):
        print("Execute using vscode")

class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()

p=Programmer()   #gives importance to the two functionalities--compile and execute rather than the class(Pycharm,Vscode)
pyc=Pycharm()
p.coding(pyc)

#OR
# p=Programmer()
# vs=Vscode()
# p.coding(vs)
