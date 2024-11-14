from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with the name '{author_name}'"

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Many-to-Many relation
        return books
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'"

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        librarian = Librarian.objects.get(library=library_name)
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to the library '{library_name}'"

from relationship_app.query_samples import get_books_by_author, get_books_in_library, get_librarian_for_library

# Query all books by a specific author
print(get_books_by_author("Author Name"))

# List all books in a library
print(get_books_in_library("Library Name"))

# Retrieve the librarian for a library
print(get_librarian_for_library("Library Name"))
