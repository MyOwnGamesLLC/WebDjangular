# Generated by Django 2.1.7 on 2019-04-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0041_auto_20190327_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='class_type',
            field=models.CharField(choices=[('button', 'Button'), ('text', 'Text'), ('textArea', 'Text Area'), ('select', 'Select'), ('ngSelect', 'NG Select'), ('codeEditor', 'CodeEditor'), ('label', 'Label'), ('switch', 'Switch (ON/OFF)'), ('checkbox', 'Checkbox')], default='text', max_length=32),
        ),
    ]
