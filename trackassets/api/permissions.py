from rest_framework.permissions import BasePermission


class IsCompanyOwner(BasePermission):

    def has_permission(self, request, view):
        isTrue = bool(request.user and request.user.is_authenticated)
        if isTrue:
            try:
               request.user.company
            except Exception as e:
                return False
        return True



class IsCompanyEmployee(BasePermission):

    def has_permission(self, request, view):
        isTrue = bool(request.user and request.user.is_authenticated)
        if isTrue:
            try:
               request.user.company
            except Exception as e:
                return False
        return True


