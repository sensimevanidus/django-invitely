# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invitely', '0002_auto_20141125_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitationusage',
            name='session_key',
            field=models.CharField(default='', max_length=40, verbose_name='session key'),
            preserve_default=False,
        ),
    ]
