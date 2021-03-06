from django.template import Context, Template
from django.template.base import Lexer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_json_api.views import ModelViewSet, RelationshipView

from webdjango.configs import CONFIG_HOME_PAGE
from webdjango.filters import WebDjangoFilterSet
from webdjango.models.Core import CoreConfig

from ..configs import CMSCoreConfig
from ..models.Block import Block
from ..models.Page import Page, PageCategory, PageTag
from ..serializers.PageSerializer import (PageCategorySerializer,
                                          PageSerializer, PageTagSerializer)
from ..signals import post_get_page, pre_get_page

from webdjango.views.CoreViewSet import CachedModelViewSet

class PageTagFilter(WebDjangoFilterSet):
    class Meta:
        model = PageTag
        fields = {
            'id': ['in'],
            'name': ['contains', 'exact'],
            'description': ['contains'],
        }


class PageTagViewSet(ModelViewSet):
    """
    Handles:
    Creating Page Tags
    Retrieve a list of Page Tags
    Retrieve a specific Page Tag
    Update Page Tags
    Deleting Page Tags
    """
    serializer_class = PageTagSerializer
    queryset = PageTag.objects.all()
    ordering_fields = '__all__'
    filter_class = PageTagFilter
    search_fields = ('name',)


class PageCategoryFilter(WebDjangoFilterSet):
    class Meta:
        model = PageCategory
        fields = {
            'id': ['in'],
            'name': ['contains', 'exact'],
            'description': ['contains'],
        }


class PageCategoryViewSet(ModelViewSet):
    """
    Handles:
    Creating Page Categories
    Retrieve a list of Page Categories
    Retrieve a specific Page Category
    Update Page Categories
    Deleting Page Categories
    """
    serializer_class = PageCategorySerializer
    queryset = PageCategory.objects.all()
    ordering_fields = '__all__'
    filter_class = PageCategoryFilter
    search_fields = ('name',)


class PageFilter(WebDjangoFilterSet):
    class Meta:
        model = Page
        fields = {
            'id': ['in'],
            'page_class': ['in', 'exact'],
            'title': ['contains', 'exact'],
            'slug': ['contains', 'exact'],
            'content': ['contains'],
        }


class PageViewSet(CachedModelViewSet):
    """
    Handles:
    Creating Pages
    Retrieve a list of Pages
    Retrieve a specific Page
    Update Pages
    Deleting Pages
    """
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    ordering_fields = '__all__'
    filter_class = PageFilter
    search_fields = ('title', 'content', 'slug')
    recursive_block = 0
    public_views = ('get_home', 'get_page')

    def send_pre_get_page(self, request, *args):
        new_kwargs = pre_get_page.send(
            sender=Page.__class__, request=request, *args, **self.kwargs)
        if new_kwargs:
            for func, data in new_kwargs:
                if data:
                    self.kwargs.update(data)

    def send_post_get_page(self, instance, request, *args):
        new_data = post_get_page.send(
            sender=Page.__class__, instance=instance, request=request, *args, **self.kwargs)
        if new_data:
            for func, new_instance in new_data:
                # TODO: improve as we are only accepting one return
                if new_instance:
                    return new_instance
        return instance

    def update_block_codes(self, content, request, layout=None):
        """
            Using Django Template Capabilites we will pre-render a little bit of the blocks to facilitate for the frontend thus reducing the number of requests
            TODO: Improvement make blocks Do the same
        """
        # Here we update the Layout
        new_content = None
        if layout:
            new_content = content
            content = layout.content

        # Here we Search for Blocks
        lexer = Lexer(content)
        tokens = lexer.tokenize()
        filter_query = []
        self.recursive_block = self.recursive_block + 1
        for token in tokens:
            if token.token_type.value == 1:
                filter_query.append(token.contents)

        if len(filter_query) > 0 and self.recursive_block <= 6:
            blocks = Block.objects.filter(
                slug__in=filter_query).values_list('slug', 'content')
            ctx = {}
            for code, data in blocks:
                ctx[code] = self.update_block_codes(data, request)

            if new_content:
                ctx['content'] = self.update_block_codes(new_content, request)
            context = Context(ctx, autoescape=False)
            body = Template(content)

            return body.render(context)
        return content

    @action(methods=['GET'], detail=True, url_path='get_page', lookup_field='slug', lookup_url_kwarg='slug')
    @method_decorator(cache_page(86400, key_prefix='get_page'))
    @method_decorator(vary_on_cookie)
    def get_page(self, request, *args, **kwargs):
        assert 'pk' in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, 'pk')
        )
        self.kwargs['slug'] = self.kwargs['pk']

        self.send_pre_get_page(request, *args)

        self.lookup_field = 'slug'
        self.lookup_url_kwarg = 'slug'
        instance = self.get_object()

        instance.content = self.update_block_codes(
            content=instance.content, request=request, layout=instance.getLayout())
        self.send_post_get_page(instance=instance, request=request, *args)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='get_home')
    @method_decorator(cache_page(86400, key_prefix='get_home'))
    @method_decorator(vary_on_cookie)
    def get_home(self, request, format=None, *args, **kwargs):
        """
        Return the Home Page
        """
        self.kwargs['pk'] = CoreConfig.read(slug=CMSCoreConfig.GROUP_SLUG+"."+CONFIG_HOME_PAGE,
                                            website=request.website)

        self.send_pre_get_page(request, *args)

        instance = self.get_object()
        instance.content = self.update_block_codes(
            content=instance.content, request=request, layout=instance.getLayout())

        self.send_post_get_page(instance=instance, request=request, *args)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PageRelationshipView(RelationshipView):
    queryset = Page.objects
