# Generated by Django 2.1.4 on 2018-12-13 13:56

import dirtyfields.dirtyfields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import djongo.models.json
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_author',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CoreConfig',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('value', djongo.models.json.JSONField(max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_config',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('name', models.CharField(max_length=100)),
                ('current_version', models.CharField(max_length=50, null=True)),
                ('version', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plugins', to='webdjango.Author')),
            ],
            options={
                'db_table': 'core_plugin',
                'ordering': ['-created'],
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('name', models.CharField(max_length=100)),
                ('angular_module', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=50)),
                ('current_version', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='webdjango.Author')),
                ('parent_theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='webdjango.Theme')),
            ],
            options={
                'db_table': 'core_theme',
                'ordering': ['-created'],
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', editable=False, primary_key=True, serialize=False)),
                ('domain', models.URLField(unique=True)),
                ('code', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_website',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='coreconfig',
            name='website',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Configs', to='webdjango.Website'),
        ),
    ]