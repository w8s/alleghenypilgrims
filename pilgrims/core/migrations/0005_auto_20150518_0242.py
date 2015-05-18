# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150518_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='name',
        ),
        migrations.AddField(
            model_name='conference',
            name='theme',
            field=models.CharField(default='The Theme', max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conference',
            name='date_end',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conference',
            name='date_start',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
