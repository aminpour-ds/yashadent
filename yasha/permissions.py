from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsAdminOrPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff and request.method in permissions.SAFE_METHODS:
            return True
        return True
