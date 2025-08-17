from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	content = models.TextField()
	published_date =models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title =models.CharField(max_length=200)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    email = models.CharField(max_length=200)