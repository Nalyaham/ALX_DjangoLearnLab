from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter() 
router.register(r'posts_all', PostViewSet, basename='posts_all')
router.register(r'Comments_all', CommentViewSet, basename='comments_all')
                
urlpatterns = [
    path('', include(router.urls)),
]