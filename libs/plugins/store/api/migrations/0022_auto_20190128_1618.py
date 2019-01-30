# Generated by Django 2.1.4 on 2019-01-28 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20190127_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('all_carts', models.BooleanField(default=None)),
                ('enabled', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('product', models.ForeignKey(default=None, null=True, on_delete=None, related_name='terms', to='store.Product')),
            ],
            options={
                'ordering': ['-position'],
            },
        ),
        migrations.AddField(
            model_name='cartitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='class_type',
            field=models.CharField(choices=[('codeEditor', 'CodeEditor'), ('button', 'Button'), ('text', 'Text'), ('select', 'Select')], default='text', max_length=32),
        ),
        migrations.AddField(
            model_name='cart',
            name='terms',
            field=models.ManyToManyField(related_name='carts', to='store.CartTerm'),
        ),
    ]