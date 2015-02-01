# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .models import InvitationUsage
from .utils import path_is_allowed


class InvitationRequiredDecorator(object):
    def __init__(self, view_func):
        self.view_func = view_func

    def __call__(self, *args, **kwargs):
        request = args[0]

        if request.user.is_authenticated() or InvitationUsage.get_invitation_from_session(request.session.session_key) or path_is_allowed(request.path):
            return self.view_func(*args, **kwargs)
        else:
            request.session['origin_path'] = request.path
            return redirect('%s?n=%s' % (reverse('invitely_invitation'), request.path))