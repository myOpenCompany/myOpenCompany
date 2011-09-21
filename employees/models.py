from django.db import models

from django.contrib.auth.models import User


class Team(models.Model):
    '''A Company is usually composed of teams'''
    
    siglum = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=64)
    parent_team = models.ForeignKey('Team', null=True, blank=True)
    description = models.TextField()
    
    class Meta:
        ordering = ["parent_team__siglum","siglum"]

    def __unicode__(self):
        return self.siglum + ": " + self.name
        
    def get_absolute_url(self):
        return "/employees/teams/" + str(self.id)
        
        
        
    
class Employee(User):
    '''Describes an employee properties'''
    
    team = models.ForeignKey(Team)
    
    def get_absolute_url(self):
        return "/employees/employees/" + self.id