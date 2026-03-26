class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.price = 0.0

    def get_info(self):
        self.title = input("Enter book title: ")
        self.author = input("Enter author's name: ")
        self.price = float(input("Enter price of the book: "))

    def display_info(self):
        print("\nBook Title:", self.title)
        print("Author:", self.author)
        print("Price: $", self.price)

library = []

print("Welcome to the Library Management System!\n")


for i in range(5):
    print("Enter details for book number", i + 1)
    book = Book()
    book.get_info()
    library.append(book)

print("\nAll books in the library:")


for i in range(len(library)):
    print("\nBook number", i + 1)
    library[i].display_info()