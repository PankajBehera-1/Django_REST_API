from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id 
    
class UpdateOwnStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id  