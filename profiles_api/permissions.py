from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        """Check user i trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True # Allow all users to see profile (GET from af methods)
        
        return obj.id == request.user.id # Only User with a correct id can edit his profile
 
 
# class UpdateOwnStatus(permissions.BasePermission):
#     """Allow sers to update their own status"""
    
#     def has_object_permission(self, request, view, obj):
#         """Check the user is trying to update their own status"""
#         if request.method in permissions.SAFE_METHODS:
#             return True
        
#         return obj.user_profile.id == request.user.id
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
    