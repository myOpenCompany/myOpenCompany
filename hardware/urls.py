from django.conf.urls.defaults import *
from django.contrib.auth.views import logout_then_login, password_change, password_change_done

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from hardware.models import Computer
from hardware.views import ComputerDetailView


urlpatterns = patterns('',
    
    ###################################
    # Computers
    (r'^computers/$', ListView.as_view( model=Computer)),
    (r'^computers/create/$', CreateView.as_view( model=Computer, ),),
    (r'^computers/(?P<pk>\d+)/$', ComputerDetailView.as_view( model=Computer, ),),
    (r'^computers/(?P<pk>\d+)/update/$', UpdateView.as_view( model=Computer, ),),
    (r'^computers/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=Computer, ),),
    ###################################
    
    
)