class book:
    # Class variables
    pages = 90
    # Constructor

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def read(self):
        print(f"Reading {self.title} by {self.author}")

    def get_info(self):
        return f"{self.title} by {self.author}, published in {self.year}"


book1 = book("blossom", "John", 2023)
book2 = book("Python", "Jane", 2022)

print(book1.title)  # Accessing the title attribute
print(book2.author)  # Accessing the author attribute
print(book1.get_info())  # Calling the get_info method