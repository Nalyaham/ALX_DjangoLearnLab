from django.urls import path, include 
from . import views
from django.contrib import admin
from blog.views import LoginView, LogoutView, RegisterView, UserProfile, DeleteView, UpdateView, DetailView, CreateView, ListView
from blog.views import CommentDeleteView, CommentUpdateView, CommentDetailView, CommentCreateView, CommentListView
#Create patterns here 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
	path('register/', RegisterView.as_view(), name='register'), 
	path('profile/', UserProfile.as_view, name = 'profile'),
    path('posts/', ListView.as_view(), name = 'posts'),
path('post/<int:pk>/', DetailView.as_view(), name = 'detail'),
path('post/new/', CreateView.as_view(), name = 'create'),
path('post/<int:pk>/update/', UpdateView.as_view(), name = 'update'),
path('post/<int:pk>/delete/', DeleteView.as_view(), name = 'delete'),
path('posts/comment', CommentListView.as_view(), name = 'posts'),
path('comment/<int:pk>/', CommentDetailView.as_view(), name = 'detai'),
path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name = 'create'),
path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name = 'update'),
path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name = 'delete')
]