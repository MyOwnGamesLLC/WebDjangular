# Generated by Django 2.1.4 on 2018-12-09 19:01

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import djongo.models.json
import libs.plugins.store.api.models.Product
import webdjango.fields.MongoFields
import webdjango.models.AbstractModels


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('attributes', djongo.models.fields.EmbeddedModelField(model_container=libs.plugins.store.api.models.Product.ProductAttributes, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.DeleteModel(
            name='ProductCollection',
        ),
        migrations.DeleteModel(
            name='ProductVariant',
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='shippingmethod',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='product',
            name='details',
        ),
        migrations.RemoveField(
            model_name='shippingmethod',
            name='shipping_zone',
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=djongo.models.json.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='bundle_products',
            field=djongo.models.fields.ArrayReferenceField(blank=True, null=True, on_delete=djongo.models.fields.ArrayReferenceField._on_delete, related_name='bundles', to='store.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=djongo.models.fields.ArrayReferenceField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.ProductCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='language',
            field=models.CharField(default=webdjango.models.AbstractModels.default_i18n, max_length=5, validators=[webdjango.models.AbstractModels.validate_i18n]),
        ),
        migrations.AddField(
            model_name='product',
            name='product_class',
            field=models.CharField(choices=[('simple', 'simple'), ('variant', 'variant'), ('bundle', 'bundle')], default='simple', max_length=32),
        ),
        migrations.AddField(
            model_name='product',
            name='translation',
            field=djongo.models.json.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='variant_attributes',
            field=djongo.models.json.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='variants',
            field=djongo.models.fields.ArrayModelField(blank=True, default=None, model_container=libs.plugins.store.api.models.Product.BaseProduct, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='language',
            field=models.CharField(default=webdjango.models.AbstractModels.default_i18n, max_length=5, validators=[webdjango.models.AbstractModels.validate_i18n]),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='translation',
            field=djongo.models.json.JSONField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=webdjango.fields.MongoFields.MongoDecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.ProductType'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(max_length=256),
        ),
    ]
