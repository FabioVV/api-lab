from rest_framework import permissions
from globals import permission_check

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    