"""Custom permissions for API."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Allow read-only access for all users, write only for author."""

    def has_permission(self, request, view):
        """Check if user has permission to access view."""
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """Check if user has permission to access object."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user 
