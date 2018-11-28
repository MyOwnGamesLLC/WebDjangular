from django_filters.filterset import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from libs.core.cms.api.models.Block import Block
from libs.core.cms.api.serializers.BlockSerializer import BlockSerializer


class BlockFilter(FilterSet):
    class Meta:
        model = Block
        fields = {
            'id': ['in'],
            'title': ['contains', 'exact'],
            'slug': ['contains', 'exact'],
            'content': ['contains'],
        }


class BlockViewSet(ModelViewSet):
    """
    Handles:
    Creating Pages
    Retrieve a list of Pages
    Retrieve a specific Page
    Update Pages
    Deleting Pages
    """
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = BlockFilter
    permission_classes = ()
