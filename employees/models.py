import re

from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    '''A Company is usually composed of teams
    Teams are linked one to another hierarchically.
    The root Team(s) have no parent_team
    '''
    
    siglum = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=64)
    parent_team = models.ForeignKey('Team', null=True, blank=True)
    description = models.TextField()
    
    class Meta:
        '''Teams should be ordered by their parent team first'''
        ordering = ["parent_team__siglum","siglum"]

    def __unicode__(self):
        '''Returns a human readable version of the team'''
        return self.siglum + ": " + self.name
        
    def get_absolute_url(self):
        '''Returns the absolute URL to this team'''
        # FIXME:use the permalink decorator
        return "/employees/teams/" + str(self.id)
        
    def get_employees(self):
        '''Returns the list of employees belonging to this team'''
        return self.employee_set.all()
        
        
        
        
class Employee(models.Model):
    '''The Employee model stores information about an employee
    This information is visible to all authenticated users
    An employee is an extension to Django's built-in User'''
    
    user = models.OneToOneField(User)
    team = models.ForeignKey(Team)
    entry_date = models.DateField()
    
    def __unicode__(self):
        '''Returns a human readable version of the user'''
        return self.user.first_name + " " + self.user.last_name
        
    def get_absolute_url(self):
        '''Returns the absolute URL to this team'''
        # FIXME:use the permalink decorator
        return "/employees/employees/" + str(self.id)
        
        
class Confidential(models.Model):
    '''The Confidential model stores personal information about a user
    This information is intended to be only visible to users or groups having 
    specific authorizations'''
    
    user = models.OneToOneField(User)
    birth_date = models.DateField()
    personal_phone = models.CharField(max_length=32, null=True, blank=True)
    personal_email = models.CharField(max_length=128, null=True, blank=True)
    postal_address = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name