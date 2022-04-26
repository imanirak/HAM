from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DEPARTMENT_CHOICES = (
    ('Clinical Operations','Clinical Ops'),
    ('Coaching','Coaching'),
    ('Commerical','Com' ),
    ('Data','data'),
    ('Engineering', 'Eng'),
    ('Executive','Exec'),
    ('Finance','Fin'),
    ('IT', 'IT'),
    ('Legal','Legal'),
    ('Marketing','MKGT'),
    ('Member Experience','MX'),
    ('Operations','Ops'),
    ('Product','Prod'),
    ('Program & Content','P&C'),
    ('Strategic Initatives','Strat Init'),
    ('Strategy','Strat'),
    ('Talent & People','Tal&PPL')
)


STATUS_CHOICES = (
   ('NEW','NEW'),
   ('In-Repair','IR'),
   ('Shipped','S'),
   ('Damaged','D'),
   ('Repaired','R'),
   ('Junk Out','JO')
)

DEVICE_CHOICES = (
    ('MBA','MacBook Air'),
   ('MBP','MacBook Pro'),
   ('Surface','Microsoft Surface'),

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