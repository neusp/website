from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'/$', 'cms.views.main'),
)