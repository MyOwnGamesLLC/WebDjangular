# Generated by Django 2.1.4 on 2019-02-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0035_auto_20190214_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeemailconfig',
            name='id',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]
