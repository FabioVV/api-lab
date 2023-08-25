from rest_framework import permissions

class IsHimself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    