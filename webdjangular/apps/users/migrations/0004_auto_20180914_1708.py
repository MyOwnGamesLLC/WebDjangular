# Generated by Django 2.0.6 on 2018-09-14 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180912_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_list', 'Can list users'),)},
        ),
    ]
