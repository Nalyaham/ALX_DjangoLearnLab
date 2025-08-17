from django.urls import path, include 
from . import views
from django.contrib import admin
from blog.views import LoginView, LogoutView, RegisterView, UserProfile, DeleteView, UpdateView, DetailView, CreateView, ListView

#Create patterns here 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
	path('register/', RegisterView.as_view(), name='register'), 
	path('profile/', UserProfile.as_view, name = 'profile'),
    path('posts/', ListView.as_view(), name = 'posts'),
path('posts/<int:pk>/', DetailView.as_view(), name = 'detail'),
path('posts/new/', CreateView.as_view(), name = 'create'),
path('/posts/<int:pk>/edit/', UpdateView.as_view(), name = 'update'),
path('posts/<int:pk>/delete/', DeleteView.as_view(), name = 'delete'),

]