# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_type', models.IntegerField(blank=True, null=True, choices=[(1, b'investor'), (2, b'borrower')])),
                ('profile_category', models.IntegerField(blank=True, null=True, choices=[(1, b'A'), (2, b'B'), (3, b'C'), (4, b'D')])),
                ('image', models.ImageField(upload_to=b'images/')),
                ('salary', models.FloatField(null=True, blank=True)),
                ('profession', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('credits_available', models.IntegerField(default=0)),
                ('credits_spent', models.IntegerField(default=0)),
                ('total_posts', models.IntegerField(default=0)),
                ('total_successful_posts', models.IntegerField(default=0)),
                ('money_invested', models.ManyToManyField(related_name='investors', null=True, to='auth_app.Person', blank=True)),
                ('user', models.OneToOneField(related_name='authors', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
