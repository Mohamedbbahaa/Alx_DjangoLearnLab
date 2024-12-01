from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Name of the author")

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the book")
    publication_year = models.PositiveIntegerField(help_text="Year the book was published")
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
# The Author model represents an author with a unique name.
# Each Author can have multiple books associated via a one-to-many relationship.

# The Book model represents a book with a title, a publication year,
# and a ForeignKey to an Author to establish the relationship.
