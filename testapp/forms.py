from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Employee,EmployeeProfileInfo
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class PromiseForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'password','emailid','department','doj']
        widgets = {
            'doj': DateInput(),
        }
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password','first_name','last_name')


class EmployeeProfileInfoForm(forms.ModelForm):
    class Meta():
        model = EmployeeProfileInfo
        
        fields = ('department','doj')
        widgets = {
            'doj': DateInput(),
            
        }