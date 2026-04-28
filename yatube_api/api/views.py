"""Views for posts app.""""""Views for API."""
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Follow, Comment
from .serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer,
)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Save author when creating post."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for comments."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        """Return comments for specific post."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        """Save author and post when creating comment."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for groups (read-only)."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthorOrReadOnly]


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSet for follows."""

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username', 'user__username']

    def get_queryset(self):
        """Return follows for current user."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Save user when creating follow."""
        serializer.save(user=self.request.user)
