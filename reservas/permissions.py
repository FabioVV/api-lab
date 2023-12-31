from rest_framework import permissions
from usuarios.models import Usuario_tipo

class IsPowerUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id
    
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    

class IsteacherOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        pass
    
    def has_permission(self, request, view):
        if request.user.user_type == Usuario_tipo.objects.get(id = 2):
            return True
        elif request.user.is_superuser:
            return True
        elif request.user.is_staff:
            return True
        else:
            return False
    