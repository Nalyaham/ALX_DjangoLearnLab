from django.shortcuts import render
from rest_framework import permissions
from .models import  Post
from rest_framework import viewsets
from .models import Post, Comment 
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, status, permissions, filters

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class PostViewSet(viewsets.ModelViewSet): 
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
	def perform_create(self, serializer):
                serializer.save(user = self.request.user)

class CommentViewSet(viewsets.ModelViewSet): 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class feed(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(user__in=following_users)
