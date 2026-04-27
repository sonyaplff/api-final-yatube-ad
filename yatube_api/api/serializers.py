"""Serializers for API."""
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('author', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'created', 'post')


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model."""

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for Follow model."""

    user = serializers.StringRelatedField(read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow

    def validate_following(self, value):
        """Prevent user from following themselves."""
        request = self.context.get('request')
        if request and request.user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return value 
 
