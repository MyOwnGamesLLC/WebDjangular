# Generated by Django 2.0.6 on 2018-09-17 20:54

from django.db import migrations, models


def create_firstpage(apps, schema_editor):
	from webdjangular.core.cms.models.Page import Page

	Page.objects.create(title="Home", slug="home", content="<h1>Hello World! My First Page</h1>")

class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.RunPython(create_firstpage)
    ]

