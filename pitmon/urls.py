from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'pitmon.views.home'),
    url(r'^plot$', 'pitmon.views.plot'),
    url(r'^current$', 'pitmon.views.current'),
)

urlpatterns += staticfiles_urlpatterns()
