from django.urls import path, include 
from . import views
from django.contrib import admin
from blog.views import LoginView, LogoutView, RegisterView, UserProfile
#Create patterns here 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
	path('register/', RegisterView.as_view(), name='register'), 
	path('profile/', UserProfile.as_view, name = 'profile'),
]