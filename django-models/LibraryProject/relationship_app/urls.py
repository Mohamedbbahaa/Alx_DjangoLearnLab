from django.urls import path
from . import views
from .views import LibraryDetailView , SignUpView
from .views import list_books , CustomLoginView , home
from django.contrib.auth.views import LoginView , LogoutView


urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='templates/logout.html'), name='logout'),
    path('', home, name='home'),
]
