from rest_framework import permissions

class IsPowerUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.user_type == 2 or request.user.id == obj.user.id
    
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    