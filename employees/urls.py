from django.conf.urls.defaults import *
from django.contrib.auth.views import logout_then_login, password_change, password_change_done

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from employees.models import Team
from employees.views import TeamDetailView 


urlpatterns = patterns('',
    
    ###################################
    # Authentication stuff
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'employees/login.html'} ),
    (r'^logout/$', logout_then_login, ),
    (r'^change_password/$', password_change, {'template_name': 'employees/password_change_form.html','post_change_redirect' : '/employees/change_password/done/'} ),
    (r'^change_password/done/$', password_change_done, {'template_name': 'employees/password_change_done.html'} ),
    ###################################
    
    (r'^teams/$', ListView.as_view( model=Team)),
    (r'^teams/create/$', CreateView.as_view( model=Team, ),),
    (r'^teams/(?P<pk>\d+)/$', TeamDetailView.as_view( model=Team, ),),
    (r'^teams/(?P<pk>\d+)/update/$', UpdateView.as_view( model=Team, ),),
    (r'^teams/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=Team, ),),
)