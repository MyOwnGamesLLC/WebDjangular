# Generated by Django 2.1.4 on 2019-01-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_auto_20181226_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
