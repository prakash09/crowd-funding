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
            name='MmInvestment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(default=0.0)),
                ('credit_rating', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_category', models.IntegerField(blank=True, null=True, choices=[(1, b'A'), (2, b'B'), (3, b'C'), (4, b'D')])),
                ('image', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('salary', models.FloatField(null=True, blank=True)),
                ('profession', models.CharField(max_length=200, null=True, blank=True)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('state', models.CharField(max_length=100, null=True, blank=True)),
                ('credits_available', models.IntegerField(default=0)),
                ('credits_spent', models.IntegerField(default=0)),
                ('total_posts', models.IntegerField(default=0)),
                ('total_successful_posts', models.IntegerField(default=0)),
                ('money_invested', models.ManyToManyField(to='auth_app.Person', null=True, through='auth_app.MmInvestment', blank=True)),
                ('user', models.OneToOneField(related_name='persons', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mminvestment',
            name='investor',
            field=models.ForeignKey(related_name='investor', to='auth_app.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mminvestment',
            name='seeker',
            field=models.ForeignKey(related_name='seeker', to='auth_app.Person'),
            preserve_default=True,
        ),
    ]
