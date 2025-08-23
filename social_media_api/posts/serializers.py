from rest_framework import serializers
from .models import Post, Comment 
from accounts.models import CustomUser

class PostSerializer(serializers.ModelSerializer):     
    class Meta:       
        model = Post       
        fields = [ 'title' , 'author', 'created_date' , 'updated_date' ]  

class CommentSerializer(serializers.ModelSerializer):    
    posts = PostSerializer(many=True, read_only=True)
    class Meta:       
        model = Comment       
        fields = [ 'Post' , 'content', 'User', 'created_date', 'name', 'posts']
