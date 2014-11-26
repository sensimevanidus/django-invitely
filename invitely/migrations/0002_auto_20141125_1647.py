# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('invitely', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationusage',
            name='used_by',
            field=models.ForeignKey(related_name='invitation_usages', verbose_name='used by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
