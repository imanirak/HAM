from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DEPARTMENT_CHOICES = (
    ('Clinical Ops','Clinical Operations'),
    ('Coaching','Coaching'),
    ('Com' ,'Commerical'),
    ('data','Data'),
    ('Eng', 'Engineering'),
    ('Exec','Executive'),
    ('Fin','Finance'),
    ('IT', 'Information Technology'),
    ('Legal','Legal'),
    ('MKTG','Marketing'),
    ('MX','Member Experience'),
    ('Ops','Operations'),
    ('Prod','Product'),
    ('P&C','Program & Content'),
    ('Strat Init','Strategic Initatives'),
    ('Strat','Strategy'),
    ('Tal&PPL','Talent & People')
)


STATUS_CHOICES = (
   ('NEW','NEW'),
   ('IR','In-Repair'),
   ('S','Shipped'),
   ('D','Damaged'),
   ('R','Repaired'),
   ('JO','Junk Out')
)

DEVICE_CHOICES = (
    ('MBA','MacBook Air'),
   ('MBP','MacBook Pro'),
   ('S','Microsoft Surface'),
   ('M','Monitor'),

)

class Device(models.Model):
    name = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50, choices=DEVICE_CHOICES)
    serial_number = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    is_shipped = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
   
    
class Inventory(models.Model):
    total_stock = models.IntegerField()
    device = models.ManyToManyField(Device)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, choices = DEPARTMENT_CHOICES)
    devices = models.ForeignKey(Device, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
