# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150518_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='conference',
            field=models.ForeignKey(default=1, to='core.Conference'),
            preserve_default=False,
        ),
    ]
