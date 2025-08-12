from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('books/create/', views.BookCreate.as_view()),
    path('books/update/<int:pk>/', views.BookUpdate.as_view()),
    path('books/delete/<int:pk>/', views.BookDelete.as_view()),
] 
