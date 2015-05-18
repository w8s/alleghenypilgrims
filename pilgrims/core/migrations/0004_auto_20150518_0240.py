# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150518_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='theme',
        ),
        migrations.AlterField(
            model_name='conference',
            name='name',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
