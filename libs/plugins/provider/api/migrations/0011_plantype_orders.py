# Generated by Django 2.1.7 on 2019-03-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_auto_20190316_0855'),
        ('provider', '0010_reseller_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantype',
            name='orders',
            field=models.ManyToManyField(related_name='plan_types', to='store.Order'),
        ),
    ]