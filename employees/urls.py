from django.conf.urls.defaults import *
from django.contrib.auth.views import logout_then_login, password_change, password_change_done

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from employees.views import TeamList, TeamDetail, CreateTeam, UpdateTeam, DeleteTeam
from employees.views import EmployeeList, EmployeeDetail, CreateEmployee, UpdateEmployee, DeleteEmployee



urlpatterns = patterns('',
    
    ###################################
    # Authentication stuff
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'employees/login.html'} ),
    (r'^logout/$', logout_then_login, ),
    (r'^change_password/$', password_change, {'template_name': 'employees/password_change_form.html','post_change_redirect' : '/employees/change_password/done/'} ),
    (r'^change_password/done/$', password_change_done, {'template_name': 'employees/password_change_done.html'} ),
    ###################################
    
    ###################################
    # Teams
    (r'^teams/$', TeamList.as_view()),
    (r'^teams/create/$', CreateTeam.as_view()),
    (r'^teams/(?P<pk>\d+)/$', TeamDetail.as_view()),
    (r'^teams/(?P<pk>\d+)/update/$', UpdateTeam.as_view()),
    (r'^teams/(?P<pk>\d+)/delete/$', DeleteTeam.as_view()),
    ###################################
    
    ###################################
    # Employees
    (r'^employees/$', EmployeeList.as_view()),
    (r'^employees/create/$', CreateEmployee.as_view()),
    (r'^employees/(?P<pk>\d+)/$', EmployeeDetail.as_view()),
    (r'^employees/(?P<pk>\d+)/update/$', UpdateEmployee.as_view(),),
    (r'^employees/(?P<pk>\d+)/delete/$', DeleteEmployee.as_view(),),
    ###################################
)