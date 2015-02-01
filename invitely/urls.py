# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^invitation/?(?P<invitation_code>[\w|\W]+)?/?$', views.invitation, name='invitation',)
)