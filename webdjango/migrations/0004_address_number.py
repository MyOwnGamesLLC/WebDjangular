# Generated by Django 2.1.4 on 2019-01-27 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdjango', '0003_address_street_address_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='number',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
