from rest_framework.permissions import BasePermission

class PostPermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True


        if request.user == obj.owner:
            return True

        return False


class CommentPermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True

        if request.method == "DELETE":

            if request.user == obj.owner:
                return True

            if obj.post.owner ==  request.user:
                return True
            
            return False
        
        if request.user == obj.owner:
            return True
            
        return False
        