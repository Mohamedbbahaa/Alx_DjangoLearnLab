from django.urls import path
from .views import RegisterView, LoginView, ProfileView, LogoutView, follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('follow/<int:user_id>/', follow_user.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user.as_view(), name='unfollow_user'),
]
