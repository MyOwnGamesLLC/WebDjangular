# Generated by Django 2.1.7 on 2019-03-21 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_auto_20190321_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('button', 'Button'), ('text', 'Text'), ('textArea', 'Text Area'), ('select', 'Select'), ('ngSelect', 'NG Select'), ('codeEditor', 'CodeEditor'), ('label', 'Label')], default='text', max_length=255),
        ),
    ]
