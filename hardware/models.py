from django.db import models

from employees.models import Employee

class Hardware(models.Model):
    '''A base class for all hardware related classes'''
    brand = models.CharField(max_length=64)
    reference = models.CharField(max_length=64)
    serial_number = models.CharField(max_length=128)
    employee = models.ForeignKey(Employee)
    comments = models.TextField()
    
    def __unicode__(self):
        return self.brand + " " + self.reference
        
       

    
class Computer(Hardware):
    
    TYPES_CHOICES = (
        ('L','Laptop'),
        ('D','Desktop'),
    )
    
    type = models.CharField(max_length=1, choices=TYPES_CHOICES)
    
    def get_absolute_url(self):
        return "/hardware/computers/" + str(self.id)

    
class Phone(Hardware):
    
    call_number = models.CharField(max_length=32)
    
    def get_absolute_url(self):
        return "/hardware/phones/" + str(self.id)