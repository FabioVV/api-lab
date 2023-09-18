from rest_framework import permissions

class IsHimself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    






SAFE_METHODS = ['POST']

class IsAuth(permissions.BasePermission):
    """
    Checks to see if the request is a POST or if it wasnt you making the request.
    """

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or not
            request.user and
            not request.user.is_authenticated):
            return True
        return True