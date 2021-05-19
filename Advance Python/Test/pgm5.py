#5. What is method overriding give an example using Books class?

#Same method and same arguments --- child class's method overrides parent class's method
class Books:
    def details(self):
        print("Book name is Alchemist")
    def read(self):
        print("Book is with Megha")
class Read_by(Books):
    def read(self):
        print("Book is with Akhil")
b=Read_by()
b.read()

#method overloading---consider no of arguments while callling