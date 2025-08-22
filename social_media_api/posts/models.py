from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
	author = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=100)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

class Comment(models.Model):
	User = models.ForeignKey(Post, on_delete = models.CASCADE)
	Post = models.ForeignKey(Post, on_delete = models.CASCADE)
	content = models.TextField(max_length=100)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

