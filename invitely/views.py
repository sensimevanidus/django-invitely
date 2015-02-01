# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from .forms import InvitationUsageForm


def invitation(request, invitation_code=''):
    if not request.session.get('has_session'):
        request.session['has_session'] = True
    if request.user.is_authenticated():
        return redirect(request.session.get('origin_path', '/'))

    if request.POST:
        invitation_usage_form = InvitationUsageForm(request.POST)
        if invitation_usage_form.is_valid():
            invitation_usage_form.save()
            messages.add_message(request, messages.SUCCESS, _(u'Silly success message'))
            return redirect(request.session.get('origin_path', request.POST.get(settings.REDIRECT_FIELD_NAME, '/')))
        else:
            messages.add_message(request, messages.ERROR, _(u'Silly error message'))
    else:
        try:
            request.session.session_key
        except:
            request.session.save()
        invitation_usage_form = InvitationUsageForm(initial={
            'code': invitation_code,
            'session_key': request.session.session_key
        })
    return render_to_response('invitely/invitation.html', {
        'invitation_usage_form': invitation_usage_form
    }, context_instance=RequestContext(request))