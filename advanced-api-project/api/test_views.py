from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(TestCase):
    def setUp(self):
        """
        Set up test data and client before each test.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author,
        )
        self.book_url = "/api/books/"

    def test_list_books(self):
        """
        Test retrieving the list of books.
        """
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Harry Potter and the Sorcerer's Stone", str(response.data))

    def test_create_book(self):
        """
        Test creating a new book.
        """
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id,
        }
        response = self.client.post(self.book_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, data["title"])

    def test_retrieve_book(self):
        """
        Test retrieving a single book by ID.
        """
        url = f"{self.book_url}{self.book.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_update_book(self):
        """
        Test updating an existing book.
        """
        url = f"{self.book_url}{self.book.id}/"
        data = {"title": "Updated Title"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, data["title"])

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        url = f"{self.book_url}{self.book.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """
        Test filtering books by title.
        """
        url = f"{self.book_url}?title=Harry Potter"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """
        Test searching books by title.
        """
        url = f"{self.book_url}?search=Sorcerer"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """
        Test ordering books by publication year.
        """
        Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author,
        )
        url = f"{self.book_url}?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 1997)

    def test_permissions(self):
        """
        Test that only authenticated users can create, update, or delete books.
        """
        # Ensure unauthorized access is blocked for creation
        data = {"title": "Unauthorized Book", "publication_year": 2000, "author": self.author.id}
        response = self.client.post(self.book_url

    def test_create_book_with_authentication(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id,
        }
        response = self.client.post(self.book_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
