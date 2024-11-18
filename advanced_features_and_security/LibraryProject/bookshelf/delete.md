# Delete the book instance
from bookshelf.models import Book
book.delete()

# Attempt to retrieve all books to confirm deletion
Book.objects.all()
<QuerySet []>
