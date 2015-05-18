# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150518_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='theme',
            field=models.TextField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
