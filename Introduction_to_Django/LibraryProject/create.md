### Create a Book Instance

**Command:**

```python
from library.models import Book

# Create a new book instance
new_book = Book.objects.create(title="1984", author="George Orwell", published_date="1949-06-08")
new_book
