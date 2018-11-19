from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import refresh_jwt_token

from .views.UserViewSet import UserViewSet
from .views.ObtainJSONWebToken import obtain_jwt_token
from .views.GroupViewSet import GroupViewSet
from .views.GroupUserView import GroupUserView
from .views.PermissionViewSet import PermissionViewSet
from .views.PermissionGroupView import PermissionGroupView
from .views.UserRelationshipView import UserRelationshipView
from .views.GroupRelationshipView import GroupRelationshipView
from .views.UserPermissionsViewSet import UserPermissionsViewSet


router = DefaultRouter()
router.register('user', UserViewSet)
router.register('group', GroupViewSet)
router.register('permission', PermissionViewSet)
router.register('userpermissions', UserPermissionsViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^token/', obtain_jwt_token),
    url(r'^token-refresh', refresh_jwt_token),
]


