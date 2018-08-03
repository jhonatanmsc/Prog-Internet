from rest_framework import permissions


class UserReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.auth)
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            print(request.auth)
            return False


class IsOwnerPostOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user or obj.owner == request.auth.user


class IsOwnerCommentOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.post.owner == request.user
