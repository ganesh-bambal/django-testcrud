from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class Employee(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    emailid = models.EmailField()
    department = models.CharField(max_length=200,default='foo')
    doj = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})

class EmployeeProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.CharField(max_length=200,default='foo')
    doj = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('employee_edit', kwargs={'pk': self.pk})
