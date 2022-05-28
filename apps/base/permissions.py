from rest_framework import permissions


class IsAuthorOrAdmin(permissions.IsAuthenticated):
    """
    Custom permission. Only the admin or the author gets access.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


