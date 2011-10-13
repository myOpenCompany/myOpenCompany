import re

from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    '''A Company is usually composed of teams'''
    
    siglum = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=64)
    parent_team = models.ForeignKey('Team', null=True, blank=True)
    description = models.TextField()
    
    class Meta:
        '''Teams should be ordered by their parent team first'''
        ordering = ["parent_team__siglum","siglum"]

    def __unicode__(self):
        return self.siglum + ": " + self.name
        
    def get_absolute_url(self):
        return "/employees/teams/" + str(self.id)
        
    def get_employees(self):
        '''Returns the list of employees belonging to this team'''
        return self.employee_set.all()
        
        
        
    
class Employee(User):
    '''Describes an employee properties'''
    
    team = models.ForeignKey(Team)
    entry_date = models.DateField()
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name
    
    def get_absolute_url(self):
        return "/employees/employees/" + str(self.id)
    
    # In the save function, we implement our own password
    # management. If the password is already hashed in the form
    # we just dont change anything otherwise we call the set_password()
    def save(self):
        password = ""
        r = re.compile('sha1\$.*')
        if not r.match(self.password):
            password = self.password
            self.set_password(self.password)
        User.save(self)