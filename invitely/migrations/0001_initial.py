# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=255, verbose_name='invitation code')),
                ('limit', models.PositiveSmallIntegerField(default=1, verbose_name='limit')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('valid_since', models.DateTimeField(null=True, verbose_name='valid since', blank=True)),
                ('valid_until', models.DateTimeField(null=True, verbose_name='valid until', blank=True)),
                ('status', models.CharField(default=b'A', max_length=1, verbose_name='status', choices=[(b'A', 'Active'), (b'I', 'Inactive'), (b'C', 'Canceled'), (b'E', 'Expired'), (b'F', 'Finished')])),
                ('sent_by', models.ForeignKey(related_name='invitations', verbose_name='sent by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvitationUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('invitation', models.ForeignKey(related_name='usages', verbose_name='invitation', to='invitely.Invitation')),
                ('used_by', models.ForeignKey(related_name='invitation_usages', verbose_name='used by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
