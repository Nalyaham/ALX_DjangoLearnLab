from django.urls import path
from .views import RegisterView, LoginView, TokenView, follow_user, unfollow_user, feed 

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('token/', TokenView.as_view()),
        path('follow/<int:user_id>/', follow_user.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', unfollow_user.as_view(), name='unfollow'),
    path('feed/', feed.as_view(), name='feed'),
]