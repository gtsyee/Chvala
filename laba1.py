class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author 
        self.year = year     
        self.is_available = True  
    def __str__(self):
        status = "В наличии" if self.is_available else "Выдана"
        return f"[№{self.book_id}] «{self.title}» — {self.author} ({self.year}) | {status}"
class Reader:
    def __init__(self, reader_id, name):
        self.reader_id = reader_id
        self.name = name
        self.books = []
    def __str__(self):
        return f"Читатель: {self.name} (билет №{self.reader_id}), книг на руках: {len(self.books)}"