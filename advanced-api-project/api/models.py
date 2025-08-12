from django.db import models
from rest_framework import filters

# Create your models here.
#This model defines the structure of the database for the Author table
class Author(models.Model):
    name = models.CharField(max_length=100)

#This model defines the structure of the database for the Book table 
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name='books')
    publication_year = models.IntegerField(default=2025)