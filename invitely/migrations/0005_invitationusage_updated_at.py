# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitely', '0004_auto_20141125_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitationusage',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 25, 22, 59, 0, 8174, tzinfo=utc), verbose_name='updated at', auto_now=True),
            preserve_default=False,
        ),
    ]
