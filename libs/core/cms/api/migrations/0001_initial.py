# Generated by Django 2.1.4 on 2018-12-13 13:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import djongo.models.json
import libs.core.cms.api.models.Menu
import webdjango.models.TranslationModel

def init_migrations(apps, schema_editor):
    from libs.core.cms.api.models.Page import Page
    from libs.core.cms.api.models.Block import Block
    from webdjango.models.Core import CoreConfig, Website
    from webdjango.configs import CONFIG_HOME_PAGE

    header = Block.objects.create(title="Header", slug="header", content="<nav>Header</nav>")
    footer = Block.objects.create(title="Footer", slug="footer", content="<footer>Footer</footer>")

    page = Page.objects.create(title="Home", slug="Home", content="<h1>Hello World!</h1>", header=header, footer=footer)

    website = Website.objects.create(domain="http://localhost:4200/", code='default')

    CoreConfig.write(CONFIG_HOME_PAGE, page.pk, website=website)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, default=None, max_length=255, null=True)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cms_block',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, default=None, max_length=255, null=True)),
                ('wrapper_class', models.CharField(max_length=255)),
                ('items', djongo.models.fields.ArrayModelField(model_container=libs.core.cms.api.models.Menu.MenuItem)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cms_menu',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('language', models.CharField(default=webdjango.models.TranslationModel.default_i18n, max_length=5, validators=[webdjango.models.TranslationModel.validate_i18n])),
                ('translation', djongo.models.json.JSONField(default=None, null=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, default=None, max_length=255, null=True)),
                ('content', models.TextField()),
                ('footer', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, related_name='footers', to='cms.Block')),
                ('header', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, related_name='headers', to='cms.Block')),
            ],
            options={
                'db_table': 'cms_page',
                'ordering': ['-created'],
            },
        ),
        migrations.RunPython(init_migrations)
    ]