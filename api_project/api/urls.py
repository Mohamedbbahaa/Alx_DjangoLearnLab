from django.urls import path
from .views import BookList
from . import views

urlpatterns = [
    path("books/", views.BookList.as_view(), name='book-list'),
]

