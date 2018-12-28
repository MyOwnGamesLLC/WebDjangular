# Generated by Django 2.1.4 on 2018-12-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20181226_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='class_type',
            field=models.CharField(choices=[('button', 'Button'), ('codeEditor', 'CodeEditor'), ('text', 'Text'), ('ckeditor', 'CkEditor'), ('select', 'Select')], default='text', max_length=32),
        ),
    ]
