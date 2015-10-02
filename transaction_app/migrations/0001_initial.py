# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField(null=True, editable=False, blank=True)),
                ('description', models.CharField(max_length=255, verbose_name=b'Category Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('featured_image', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('interest_rate', models.FloatField(default=0.0, null=True, blank=True)),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('amount_requested', models.FloatField(default=0)),
                ('amount_received', models.FloatField(default=0)),
                ('tenure', models.IntegerField(null=True, blank=True)),
                ('slug', models.SlugField(editable=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('author_name', models.ForeignKey(related_name='posts', to='auth_app.Person')),
                ('category', models.ForeignKey(to='transaction_app.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
