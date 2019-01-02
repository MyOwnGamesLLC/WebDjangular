# Generated by Django 2.1.4 on 2018-12-26 15:12

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20181224_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattributevalue',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='data',
            field=django_mysql.models.JSONField(null=True, default=None),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='class_type',
            field=models.CharField(choices=[('button', 'Button'), ('ckeditor', 'CkEditor'), ('select', 'Select'), ('codeEditor', 'CodeEditor'), ('text', 'Text')], default='text', max_length=32),
        ),
        migrations.DeleteModel(
            name='ProductAttributeValue',
        ),
    ]