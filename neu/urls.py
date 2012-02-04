import settings

from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url

admin.autodiscover()

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT,
          'show_indexes':True}),
    )

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('neu.cms.urls')),
)
