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
            name='Conference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('theme', models.TextField(blank=True)),
                ('date_start', models.DateField(blank=True)),
                ('date_end', models.DateField(blank=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('is_current', models.BooleanField(default=False)),
                ('location_address', models.TextField(blank=True)),
                ('location_name', models.TextField(blank=True)),
                ('map_link', models.CharField(max_length=255, blank=True)),
                ('user_updated', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
