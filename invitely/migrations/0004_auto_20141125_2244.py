# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invitely', '0003_invitationusage_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationusage',
            name='session_key',
            field=models.CharField(unique=True, max_length=40, verbose_name='session key'),
            preserve_default=True,
        ),
    ]
