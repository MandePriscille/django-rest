from rest_framework import permissions

class IsStaffPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            if user.has_perm('product.add_product'):
                return True
            if user.has_perm('product.change_product'):
                return True
            if user.has_perm('product.delete_product'):
                return True
            if user.has_perm('product.view_product'):
                return True
        return False
        