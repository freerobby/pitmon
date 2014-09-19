from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'pitmon.views.home'),
    url(r'^current$', 'pitmon.views.current'),
    url(r'^data$', 'pitmon.views.data'),
)

urlpatterns += staticfiles_urlpatterns()
