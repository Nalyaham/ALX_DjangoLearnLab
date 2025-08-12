import django_filters
from .models import Book, Author 

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
