from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photos_backend.views.home', name='home'),
    url(r'^api/', include('photos_backend.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

