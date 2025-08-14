from django.urls import path, include 
from . import views
from django.contrib import admin

#Create patterns here 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]