from django.conf.urls.defaults import patterns
from models import Page

urlpatterns = patterns('',
    ('', 'cms.views.main')
)
