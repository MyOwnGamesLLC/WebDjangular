from rest_framework.serializers import ModelSerializer

from libs.core.cms.api.models.Page import Page


class PageSerializer(ModelSerializer):
    """
    The serializer for Pages Objects
    """
    
    class Meta:
        model = Page
        fields = ('title', 'slug', 'content')