# Generated by Django 2.1.4 on 2019-01-22 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdjango', '0002_auto_20181222_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='street_address_3',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
