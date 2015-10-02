# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='profile_type',
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='profession',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(related_name='persons', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
