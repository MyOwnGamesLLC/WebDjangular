# Generated by Django 2.1.7 on 2019-04-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdjango', '0012_email_email_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='subject',
            field=models.CharField(default='Label', max_length=1024),
        ),
    ]
