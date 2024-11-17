from django.urls import path
from . import views
from .views import LibraryDetailView , SignUpView
from .views import list_books
from django.contrib.auth.views import LoginView , LogoutView


urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', SignUpView.as_view(template_name='templates/relationship_app/register.html'), name='register'),
    path('', LoginView.as_view(template_name='templates/relationship_app/login.html'), name='login'),
    path('', LogoutView.as_view(template_name='templates/relationship_app/logout.html'), name='logout'),
]
