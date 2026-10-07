from rest_framework.permissions import BasePermission

class PostPermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True


        if request.user == obj.owner:
            return True

        return False
        