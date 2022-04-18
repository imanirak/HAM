from django.db import models
from django.contrib.auth.models import User
# Create your models here.

DEPARTMENT_CHOICES = (
    ('Clinical Operations'),
    ('Coaching'),
    ('Commerical'),
    ('Data'),
    ('Engineering'),
    ('Executive'),
    ('Finance'),
    ('IT'),
    ('Legal'),
    ('Marketing'),
    ('Member Experience'),
    ('Operations'),
    ('Product'),
    ('Program & Content'),
    ('Strategic Initatives'),
    ('Strategy'),
    ('Talent & People')
)


STATUS_CHOICES = (
   ('NEW'),
   ('In-Repair'),
   ('Shipped'),
   ('Damaged'),
   ('Repaired'),
   ('Junk Out')
)


class Device(models.Model):
    device_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    
    

class Employee(models.Model):
    user = models.OneToOneField(User, one_delete=models.CASCADE)
    department = models.CharField(max_length=10, choices = DEPARTMENT_CHOICES)
    devices = models.ManyToManyField(Device)
    
class Inventory(models.Model):
    total_stock = models.IntegerField()
    
    

