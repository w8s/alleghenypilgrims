# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_speaker_conference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='profile',
            field=models.TextField(max_length=400),
            preserve_default=True,
        ),
    ]
