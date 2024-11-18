book = Book.objects.get(title="1984")
book.title, book.author, book.published_date
('1984', 'George Orwell', datetime.date(1949, 6, 8))

