# Generated by Django 2.0.6 on 2018-09-21 12:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import re

def start_config_data(apps, scheme_editor):
    from webdjangular.webdjango.models.Core import CoreConfig, Website
    from webdjangular.core.cms.models.Page import Page
    from webdjangular.webdjango.configs import CONFIG_HOME_PAGE

    website, created = Website.objects.get_or_create(
        domain='http://localhost:4200/',
        code='default'
    )
    page, created = Page.objects.get_or_create(title="Home", slug="home", content="<h1>Hello World! My First Page</h1>")
    CoreConfig.write(CONFIG_HOME_PAGE, page.pk, website)

class Migration(migrations.Migration):

    dependencies = [
        ('webdjango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('value', models.TextField(max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_config',
                'permissions': (('list_core_config', 'Can list core_config'),),
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField(unique=True)),
                ('code', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_website',
                'permissions': (('list_core_website', 'Can list core_website'),),
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('list_core_authors', 'Can list core_author'),)},
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'permissions': (('list_core_themes', 'Can list core_theme'),)},
        ),
        migrations.AlterField(
            model_name='app',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
        migrations.AlterField(
            model_name='theme',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
        migrations.AddField(
            model_name='coreconfig',
            name='website',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Configs', to='webdjango.Website'),
        ),
        migrations.RunPython(start_config_data)
    ]