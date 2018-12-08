from libs.plugins.provider.api.models.City import City, Streets, NumberRange
from rest_framework_json_api import serializers
from webdjango.serializers.MongoSerializer import EmbeddedSerializer, ArrayModelFieldSerializer


class NumberRangeSerializer(EmbeddedSerializer):
    start = serializers.IntegerField()
    end = serializers.IntegerField()
    class Meta:
        model = NumberRange



class StreetSerializer(EmbeddedSerializer):
    name = serializers.CharField()
    short_name = serializers.CharField()
    numbers = ArrayModelFieldSerializer(
        serializer = NumberRangeSerializer
    )
    class Meta:
        model = Streets



class CitySerializer(serializers.ModelSerializer):
    postal_codes = ArrayModelFieldSerializer(
        serializer = NumberRangeSerializer
    )
    streets = ArrayModelFieldSerializer(
        serializer = StreetSerializer
    )
    class Meta:
        model = City
        fields = '__all__'
