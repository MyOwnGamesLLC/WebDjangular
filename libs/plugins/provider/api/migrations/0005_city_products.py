# Generated by Django 2.1.4 on 2019-01-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20190122_1735'),
        ('provider', '0004_auto_20190103_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='products',
            field=models.ManyToManyField(to='store.Product'),
        ),
    ]