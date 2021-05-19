# 3. Create a Book class with instance Library_name, book_name, author, pages?
#instances---arguments
class Book:
    Library_name="Regal Libraries"
    def details(self,book_name,author,pages):
        self.book_name=book_name
        self.author=author
        self.pages=pages
        print("Library Name:",Book.Library_name)
        print("Book name:",self.book_name)
        print("Author:",self.author)
        print("Pages:",self.pages)
bk=Book()
bk.details("Alchemist","Paulo Coehlo",365)
