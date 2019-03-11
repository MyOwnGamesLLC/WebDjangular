from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework_json_api.views import ModelViewSet, RelationshipView

from libs.core.cms.api.models.Form import (Form, FormAction, FormField,
                                           FormSubmition)
from libs.core.cms.api.serializers.FormSerializer import (FormActionSerializer,
                                                          FormFieldSerializer,
                                                          FormSerializer,
                                                          FormSubmitionSerializer)
from webdjango.filters import WebDjangoFilterSet


class FormFilter(WebDjangoFilterSet):
    class Meta:
        model = Form
        fields = {
            'id': ['in'],
            'slug': ['in', 'exact'],
        }


class FormViewSet(ModelViewSet):
    """
    Handles:
    Creating Pages
    Retrieve a list of Pages
    Retrieve a specific Page
    Update Pages
    Deleting Pages
    """
    serializer_class = FormSerializer
    queryset = Form.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = '__all__'
    filter_class = FormFilter


class FormRelationshipView(RelationshipView):
    queryset = Form.objects.all()


class FormSubmitionViewSet(ModelViewSet):
    """
    Handles:
    Creating Pages
    Retrieve a list of Pages
    Retrieve a specific Page
    Update Pages
    Deleting Pages
    """
    serializer_class = FormSubmitionSerializer
    queryset = FormSubmition.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = '__all__'


class FormSubmitionRelationshipView(RelationshipView):
    queryset = FormSubmition.objects.all()


class FormActionViewSet(ModelViewSet):
    """
    Handles:
    Creating Pages
    Retrieve a list of Pages
    Retrieve a specific Page
    Update Pages
    Deleting Pages
    """
    serializer_class = FormActionSerializer
    queryset = FormAction.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = '__all__'


class FormActionRelationshipView(RelationshipView):
    queryset = FormAction.objects.all()


class FormFieldViewSet(ModelViewSet):
    """
    Handles:
    Creating Pages
    Retrieve a list of Pages
    Retrieve a specific Page
    Update Pages
    Deleting Pages
    """
    serializer_class = FormFieldSerializer
    queryset = FormField.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = '__all__'


class FormFieldRelationshipView(RelationshipView):
    queryset = FormField.objects.all()
