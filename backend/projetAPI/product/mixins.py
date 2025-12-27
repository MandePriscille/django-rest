from .permissions import IsStaffPermissions
from rest_framework import permissions

class StaffEditorPermissionsMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffPermissions]
