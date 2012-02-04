#!/usr/bin/env python

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../../'))

import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
