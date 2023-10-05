from rest_framework import permissions
from usuarios.models import Usuario_tipo


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if(obj.user == request.user):
            return True
        elif(request.user.is_superuser):
            return True
        else:
            return False
         
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    

class IsTeacherOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #tipo_user = Usuario_tipo.objects.get(id = request.user.user_type)
        pass
         
    
    def has_permission(self, request, view):
        if(request.user.user_type == 2):
            return True
        elif(request.user.is_superuser ):
            return True
        else:
            return False
        
        return super().has_permission(request, view)
    


    