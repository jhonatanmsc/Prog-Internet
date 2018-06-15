from rest_framework import permissions
from perfil.models import Post, Profile


class ReadUserOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True if request.method in permissions.SAFE_METHODS else False

class IsOwnerOfCommentOrManagerOfPost(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            id = obj.post_id
            post = Post.objects.get(id=id.id)
            user = Profile.objects.get(id=post.userId.id)
            return request.profile in user.profiles.all()

class IsOwnerOfPostOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True if request.method in permissions.SAFE_METHODS else False


class IsOneProfileOfTheUserOrAccessDenied(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True if request.method in permissions.SAFE_METHODS else False


