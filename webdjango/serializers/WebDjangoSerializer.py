from django.utils.functional import empty
from rest_framework_json_api import serializers
# from rest_framework import serializers
from ..signals.SerializerSignals import pre_init_serializer, post_init_serializer


class WebDjangoSerializer(serializers.ModelSerializer):
    """
    A Document Serializer For Nested Documents
    """

    def __init__(self, *args, **kwargs):
        pre_init_serializer.send(
            sender=self.__class__, serializer=self, args=args, kwargs=kwargs)
        super(WebDjangoSerializer, self).__init__(*args, **kwargs)
        post_init_serializer.send(
            sender=self.__class__, serializer=self, args=args, kwargs=kwargs)
