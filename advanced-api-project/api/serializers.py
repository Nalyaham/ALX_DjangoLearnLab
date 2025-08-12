from rest_framework import serializers 
from api.models import Book, Author 
from datetime import date 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ['title', 'author','publication_year']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) #This attribute is used to serialize the Book model

    class Meta:
        model = Author 
        fields = ['title', 'author', 'publication_year', 'name', 'books'] #The attribute is declared among the fields that will be serializer by this serializer 

    def validate_date(self, date): 
         if date > date.today():
             raise serializers.ValidationError("Date is in the future")
         return date 

        