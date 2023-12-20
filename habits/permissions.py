from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем!'

    def has_permission(self, request, view):
        return request.user == view.get_object().owner
