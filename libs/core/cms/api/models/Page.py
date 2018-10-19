from djongo.models import Model
from django.db import models as djangoModels


class Page(Model):
    """
    CMS Pages Model
    """
    title = djangoModels.CharField(max_length=255)
    slug = djangoModels.SlugField(
        max_length=255, null=True, default=None, blank=True)
    content = djangoModels.TextField()
    created = djangoModels.DateTimeField(auto_now_add=True)
    updated = djangoModels.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cms_page'
        ordering = ['-id']
        permissions = (("list_pages", "Can list pages"),)