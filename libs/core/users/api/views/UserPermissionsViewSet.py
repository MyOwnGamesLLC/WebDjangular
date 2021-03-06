from django.contrib.auth.models import Permission
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from libs.core.users.api.models import User
from libs.core.users.api.serializers.PermissionSerializer import \
    PermissionSerializer
from libs.core.users.api.serializers.UserSerializer import UserSerializer


class UserPermissionsViewSet(ListModelMixin, GenericViewSet):
    resource_name = 'user'
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        perms = []

        if request.user.is_staff == True:
            allPerms = Permission.objects.all()
            serializer = PermissionSerializer(allPerms, many=True)
        else:
            userPermissions = request.user.get_all_permissions()

            for userPerm in userPermissions:
                parts = userPerm.split(".")
                perm = Permission.objects.filter(codename=parts[1]).filter(
                    content_type__app_label=parts[0])

                if perm.count() > 0:
                    perms.append(perm.get())

            serializer = PermissionSerializer(perms, many=True)

        return Response(serializer.data)
