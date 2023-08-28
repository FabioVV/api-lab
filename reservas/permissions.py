from rest_framework import permissions

class IsPoweUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.user_type == 2 or request.user.user_type == obj.user.user_type
    
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    