# Generated by Django 2.1.4 on 2019-01-02 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20181227_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='alt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cms.MenuItem'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.SlugField(),
        ),
    ]
