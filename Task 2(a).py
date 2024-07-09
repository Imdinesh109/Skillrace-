class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        self._author = author
    @property
    def publisher(self):
        return self._publisher
    @publisher.setter
    def publisher(self, publisher):
        self._publisher = publisher
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price
    def royalty(self, copies_sold):
        if copies_sold <= 500:
            return 0.10 * self._price * copies_sold
        elif copies_sold <= 1500:
            return (0.10 * self._price * 500) + (0.125 * self._price * (copies_sold - 500))
        else:
            return (0.10 * self._price * 500) + (0.125 * self._price * 1000) + (0.15 * self._price * (copies_sold - 1500))
class EBook(Book):
    def __init__(self, title, author, publisher, price, format):
        super().__init__(title, author, publisher, price)
        self._format = format
    @property
    def format(self):
        return self._format
    @format.setter
    def format(self, format):
        self._format = format
    def royalty(self, copies_sold):
        base_royalty = super().royalty(copies_sold)
        gst_deducted = base_royalty * 0.88  
        return gst_deducted
book = Book("Sample Book", "Author Name", "Publisher Name", 100)
ebook = EBook("Sample EBook", "Author Name", "Publisher Name", 100, "EPUB")
print(book.royalty(2000))  
print(ebook.royalty(2000)) 