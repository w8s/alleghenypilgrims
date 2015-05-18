# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_speaker'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
