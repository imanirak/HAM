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
    ('IT', 'IT'),
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

)

SHIPSTATUS_CHOICES = (
    ('Y','Yes'),
     ('N','No'),
   ('WO','With Owner'),
   ('WC','With Company'),


)

    

    
    
class Device(models.Model):
    name = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50, choices=DEVICE_CHOICES)
    serial_number = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    ship_status = models.CharField(max_length=50, choices=SHIPSTATUS_CHOICES)
    
    def __str__(self):
        return self.name
    
    
   
class Inventory(models.Model):
    name = models.CharField(max_length=50, choices=DEVICE_CHOICES)
    in_stock = models.PositiveIntegerField(default=0)
    devices = models.ManyToManyField(Device,blank=True)
    add = models.PositiveIntegerField(default=0)
    
    
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    department = models.CharField(max_length=50, choices =DEPARTMENT_CHOICES)
    is_manager = models.BooleanField(default=False)
    devices = models.ManyToManyField(Device,blank=True)
    
    
    def __str__(self):
        return self.name