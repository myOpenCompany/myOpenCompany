from django import forms

from employees.models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('username','first_name','last_name','email','team','password','is_staff','is_active','is_superuser')
        widgets = {'password':forms.PasswordInput()}
        
    #def save(self,)