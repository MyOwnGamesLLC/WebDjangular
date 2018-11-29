# Generated by Django 2.0.6 on 2018-11-29 13:55

from django.db import migrations, models
import djongo.models.fields
import libs.plugins.provider.api.models.City


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='code',
            field=models.SlugField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='short_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='streets',
            field=djongo.models.fields.ArrayModelField(default=None, model_container=libs.plugins.provider.api.models.City.Streets, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='zips',
            field=djongo.models.fields.ArrayModelField(default=None, model_container=libs.plugins.provider.api.models.City.NumberRange, null=True),
        ),
    ]
