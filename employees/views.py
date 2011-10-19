from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User

from employees.models import Team, Employee


####################################
# Team Views

class TeamList(ListView):
    
    model = Team

    

class TeamDetail(DetailView):
    
    model = Team
    
    

class CreateTeam(CreateView):
    
    model = Team
    


class UpdateTeam(UpdateView):
    
    model = Team
    

    
class DeleteTeam(DeleteView):
    
    model = Team

####################################


####################################
# Employee Views
    
    
class EmployeeList(ListView):
    
    model = Employee

    

class EmployeeDetail(DetailView):
    
    model = Employee
    
    

class CreateEmployee(CreateView):
    
    model = Employee
    


class UpdateEmployee(UpdateView):
    
    model = Employee
    

    
class DeleteEmployee(DeleteView):
    
    model = Employee
    
####################################