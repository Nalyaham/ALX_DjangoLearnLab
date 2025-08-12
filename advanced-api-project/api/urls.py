from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('books/create/', views.BookCreate.as_view()),
    path('books/<int:pk>/update/', views.BookUpdate.as_view()),
    path('books/<int:pk>/delete/', views.BookDelete.as_view()),
] 
