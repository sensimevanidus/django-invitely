# -*- coding: utf-8 -*-
import random
from django.db import models, IntegrityError
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Invitation(models.Model):
    code = models.CharField(_(u'invitation code'), max_length=255, unique=True,)
    sent_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'sent by'), related_name='invitations',)
    limit = models.PositiveSmallIntegerField(_(u'limit'), default=1,)
    created_at = models.DateTimeField(_(u'created at'), auto_now_add=True,)
    updated_at = models.DateTimeField(_(u'updated at'), auto_now=True,)
    valid_since = models.DateTimeField(_(u'valid since'), blank=True, null=True,)
    valid_until = models.DateTimeField(_(u'valid until'), blank=True, null=True,)
    status = models.CharField(_(u'status'), max_length=1, choices=(
        ('A', _(u'Active')),
        ('I', _(u'Inactive')),
        ('C', _(u'Canceled')),
        ('E', _(u'Expired')),
        ('F', _(u'Finished')),
    ), default='A',)

    def __unicode__(self):
        return self.code

    def is_valid(self):
        return 'A' == self.status

    def update_status(self):
        usage_count = self.usages.count()
        if usage_count >= self.limit:
            self.status = 'F'
            self.save()

    @staticmethod
    def generate_code():
        code = ''.join(random.choice('0123456789') for i in range(6))
        while Invitation.objects.filter(code=code).exists():
            code = ''.join(random.choice('0123456789') for i in range(6))
        return code


class InvitationUsage(models.Model):
    invitation = models.ForeignKey(Invitation, verbose_name=_(u'invitation'), related_name='usages',)
    used_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'used by'), related_name='invitation_usages', blank=True, null=True,)
    session_key = models.CharField(_(u'session key'), max_length=40, unique=True,)
    created_at = models.DateTimeField(_(u'created at'), auto_now_add=True,)
    updated_at = models.DateTimeField(_(u'updated at'), auto_now=True,)

    def __unicode__(self):
        return u'%s - %s' % (unicode(self.invitation), unicode(self.used_by))

    @staticmethod
    def get_invitation_from_session(session_key):
        try:
            return InvitationUsage.objects.get(session_key=session_key,)
        except InvitationUsage.DoesNotExist:
            return None