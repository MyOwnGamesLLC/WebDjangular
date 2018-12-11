from ..exceptions import InsufficientStock
from decimal import Decimal
from django.conf import settings
from django_measurement.models import MeasurementField
from djongo import models
from djongo.models.json import JSONField
from flex.loading.common import max_length
from libs.core.utils.api.weight import WeightUnits, zero_weight
from libs.plugins.store.api import defaults
from measurement.measures import Weight
from webdjango.fields.MongoFields import MongoDecimalField
from webdjango.models.AbstractModels import ActiveModel, DateTimeModel, \
    PermalinkModel, TranslationModel
from webdjango.models.CoreConfig import CoreConfigInput




class ProductClasses:
    SIMPLE = 'simple'
    VARIANT = 'variant'
    BUNDLE = 'bundle'

    CHOICES = [
        (SIMPLE, 'simple'),
        (VARIANT, 'variant'),
        (BUNDLE, 'bundle')
    ]


class ProductCategory(PermalinkModel, TranslationModel, DateTimeModel):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    # parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    i18n_fields = ['name', 'slug', 'description']

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.name)

class ProductAttributes(models.Model):
    slug = models.SlugField()
    name = models.CharField()
    required = models.BooleanField(default=False)
    type = models.CharField(max_length=32, choices=CoreConfigInput.CONFIG_FIELD_TYPES, default=CoreConfigInput.FIELD_TYPE_TEXT)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.name)


class ProductType(DateTimeModel):
    name = models.CharField(max_length=128)
    attributes = models.EmbeddedModelField(model_container=ProductAttributes)
    ## TODO: If ProductType is Update we need to update all the Product Childrens, Or Make a Lazy Load of this Update

    ## TODO: Work on some way to Translate The Product Attributes, Maybe create a Product Attribute Translation Table?
    class Meta:
        ordering = ['-id']



class ProductDimensions(models.Model):
    # TODO: change to MeasuramentField
    width = models.CharField(max_length=32)
    height = models.CharField(max_length=32)
    depth = models.CharField(max_length=32)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s object (w:%s,h:%s,d:%s)' % (self.__class__.__name__, self.width, self.height, self.depth)


class ProductShipping(models.Model):
    weight = MeasurementField(measurement=Weight,
                              unit_choices=WeightUnits.CHOICES,
                              default=zero_weight)
    dimensions = models.EmbeddedModelField(model_container=ProductDimensions, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.dimensions)

class ProductPricing(models.Model):
    list = MongoDecimalField(
        max_digits=defaults.DEFAULT_MAX_DIGITS,
        decimal_places=defaults.DEFAULT_DECIMAL_PLACES
    )
    sale = MongoDecimalField(
        max_digits=defaults.DEFAULT_MAX_DIGITS,
        decimal_places=defaults.DEFAULT_DECIMAL_PLACES
    )
    # TODO: tier prices

    class Meta:
        abstract = True

    def __str__(self):
        return '%s object (List:%s,Sale:%s)' % (self.__class__.__name__, self.list, self.sale)


class BaseProduct(ActiveModel, DateTimeModel, PermalinkModel, TranslationModel, ):
    sku = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    description = models.TextField(blank=True)

    available_on = models.DateTimeField(blank=True, null=True)

    track_inventory = models.BooleanField(default=True)
    quantity = models.IntegerField(default=Decimal(1))
    quantity_allocated = models.IntegerField(default=Decimal(0))
    cost = MongoDecimalField(
        max_digits=defaults.DEFAULT_MAX_DIGITS,
        decimal_places=defaults.DEFAULT_DECIMAL_PLACES
    )



    pricing = models.EmbeddedModelField(model_container=ProductPricing)
    # TODO: The Validation of this Field should be realted to the Product Type
    attributes = JSONField(default=None, blank=True, null=True)



    i18n_fields = ['name', 'slug', 'description']


    class Meta:
        abstract = True


class Product(BaseProduct):
    product_class = models.CharField(max_length=32, choices=ProductClasses.CHOICES, default=ProductClasses.SIMPLE)
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, blank=True, null=True)

    #  product class VARIANT
    variants = models.ArrayModelField(model_container=BaseProduct, default=None, blank=True, null=True)
    variant_attributes = JSONField(default=None, blank=True, null=True)

    #  product class BUNDLE
    bundle_products = models.ArrayReferenceField(to='Product', on_delete=None, related_name='bundles', blank=True, null=True)

    categories = models.ArrayReferenceField(to=ProductCategory, on_delete=models.CASCADE, related_name='products', default=None, blank=True, null=True)
    class Meta:
        ordering = ['-id']


    @property
    def quantity_available(self):
        #TODO: Quanty based on Childrens
        return max(self.quantity - self.quantity_allocated, 0)

    def check_quantity(self, quantity):
        """Check if there is at least the given quantity in stock
        if stock handling is enabled.
        """
        if self.track_inventory and quantity > self.quantity_available:
            raise InsufficientStock(self)

    @property
    def base_price(self):
        # TODO: Check Based on Selected Children
        return self.pricing.sale or self.pricing.list

    @property
    def is_shipping_required(self):
        # TODO: Based on the Product Class
        return True

    @property
    def is_in_stock(self):
        return self.quantity_available > 0