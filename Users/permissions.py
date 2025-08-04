from rest_framework import permissions

class IsConductor(permissions.BasePermission):
    """
    Custom permission to allow users who has is_conductor=True
    """

    def has_permissions(self, request, view):
        return request.user and request.user.is_conductor
