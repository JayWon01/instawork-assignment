from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

# Create your models here.
class teamMember(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    PhoneNumber = PhoneNumberField()
    TYPE_SELECT = (
        ('Admin', 'Admin'),
        ('Regular', 'Regular'),
    )
    Role = models.CharField(max_length=11, choices=TYPE_SELECT)
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName

    def get_absolute_url(self):
         return reverse('list')