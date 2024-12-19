from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    #path('posts-details/', views.postData, name='posts'),
    #path('create-post/', views.createPost, name='create-post'),
    #path('comments-details/', views.commentData, name='comments'),
    path('', include(router.urls)),
]