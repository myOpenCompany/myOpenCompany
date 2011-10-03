from django.conf.urls.defaults import patterns, include, url

from views import home_view

urlpatterns = patterns('',
    (r'^$', home_view),
    (r'^employees/', include('employees.urls')),
)
