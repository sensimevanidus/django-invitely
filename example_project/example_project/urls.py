from django.conf.urls import patterns, include, url
from django.contrib import admin
from invitely.decorators import InvitationRequiredDecorator
from .helper import required

urlpatterns = required(
    InvitationRequiredDecorator,
    patterns('',
        url(r'^accounts/', include('allauth.urls')),
    )
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^invitely/', include('invitely.urls', namespace='invitely',)),
)
