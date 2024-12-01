from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

# The BookSerializer serializes all fields of the Book model.
# Includes custom validation to ensure publication year is not in the future.

# The AuthorSerializer serializes the Author model, including the name field
# and a nested list of related books serialized using the BookSerializer.
