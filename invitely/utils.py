# -*- coding: utf-8 -*-
from django.conf import settings


def path_is_allowed(path):
    allowed_paths = getattr(settings, 'INVITELY_ALLOWED_PATHS', [])
    return path in allowed_paths