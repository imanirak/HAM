from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Device, Employee, Inventory
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.db.models import F
from django.forms import Select



class Home(TemplateView):
    template_name='home.html'
 
class About(TemplateView):
    template_name='about.html'


@method_decorator(login_required, name="dispatch")
class Employee_Create(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['name','first_name', 'last_name', 'department']
    template_name = "employee_create.html"

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/devices/new')
    

@method_decorator(login_required, name="dispatch")
class Employee_List(TemplateView):
    template_name='employee_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        employees = Employee.objects.all()
        for employee in employees:
            for device in employee.devices.all():
                if device.name == employee.name:
                    print(device.name)
                    print(employee.name)
                    Select()
                if name != None:
                    context['employees']=Employee.objects.filter(name__icontains=name)
                    context['header']= f'Searching for {name}'
                else:
                    context['employees']=Employee.objects.all()
                    context['devices']=Device.objects.all()
            
            context['header']= 'Employees:'
            
        return context
    
 
@method_decorator(login_required, name="dispatch")    
class Employee_Detail(DetailView):
    model = Employee
    template_name = "employee_detail.html"
 

@method_decorator(login_required, name="dispatch")  
class Employee_Update(UpdateView):
    model = Employee
    fields = ['name','first_name', 'last_name', 'department', 'devices']
    template_name = "employee_update.html"
    def get_success_url(self):
        return reverse('employee_detail', kwargs={'pk': self.object.pk})
  
  
@method_decorator(login_required, name="dispatch")
class Employee_Delete(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = "/employees/"




@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    devices = Device.objects.filter(user=user)
    employees = Employee.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'devices': devices, 'employees':employees})

########################DEVICE################################


@method_decorator(login_required, name="dispatch")   
class Device_List(TemplateView):
    template_name='device_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        
        if name != None:
            context['devices']=Device.objects.filter(name__icontains=name)
            context['header']= f'Searching for {name}'
        else:
            context['devices']=Device.objects.all()
            context['header']= 'Devices:'
            
        return context
    
@login_required
def devices_index(request):
    devices = Device.objects.all()
    return render(request, 'devices_index.html', {'devices':devices})

@login_required
def devices_show(request, device_id):
    devices = Device.objects.get(id=device_id)
    return render(request, 'devices_show.html', {'devices': devices})

@method_decorator(login_required, name="dispatch")
class Device_Create(CreateView):
    model = Device
    fields = [ 'device_type', 'serial_number', 'model_number', 'status','ship_status']
    template_name = "device_create.html"
    devices = Device.objects.all()
    inventory = Inventory.objects.all()
    
  
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        device_type = self.object.device_type
        device = self.object
        print(device)
        #update name based on last created employee
        employee = Employee.objects.last()
        device_name = employee
        
        device.name = device_name
        device.save(['name'])
        
        # print(employee.devices.contains())
     
        if device_type == 'MBA':
            inventory_mba = Inventory.objects.filter(name='MBA')       
            inventory_mba.update(in_stock=F('in_stock') - 1)
       
        elif device_type == 'MBP':
            inventory_mbp = Inventory.objects.filter(name='MBP')     
            inventory_mbp.update(in_stock=F('in_stock') - 1)
  
            
        elif self.object.device_type == 'S' :
            inventory_s = Inventory.objects.filter(name='S')     
            inventory_s.update(in_stock=F('in_stock') - 1)

        
        return HttpResponseRedirect('/employees')


@method_decorator(login_required, name="dispatch")    
class Devices_Detail(DetailView):
    model = Device
    template_name = "devices_detail.html"
 

@method_decorator(login_required, name="dispatch")  
class Device_Update(UpdateView):
    model = Employee
    fields = ['name', 'device_type', 'serial_number', 'model_number', 'status','ship_status']
    template_name = "devices_update.html"
    def get_success_url(self):
        return reverse('devices_detail', kwargs={'pk': self.object.pk})
    

@method_decorator(login_required, name="dispatch")
class Device_Update(UpdateView):
    model = Device
    fields = ['name', 'device_type', 'serial_number', 'model_number', 'status','ship_status']
    template_name = 'devices_update.html'
    success_url = "/devices"
    
@method_decorator(login_required, name="dispatch")
class Device_Delete(DeleteView):
    model = Device
    template_name = 'devices_delete.html'
    success_url = '/devices'
  
  
  ##################### INVENTORY ##########################  
  
  
@login_required
def inventory_index(request):
    inventory = Inventory.objects.all()
    print(inventory)
    return render(request, 'inventory_index.html', {'inventory':inventory}, )


@method_decorator(login_required, name="dispatch")
def inventory_show(request, inventory_id):
    inventory = Inventory.objects.get(id=inventory_id)
    return render(request, 'inventory_show.html', {'inventory': inventory})


@method_decorator(login_required, name="dispatch")
class Inventory_Create(CreateView):
    model = Inventory
    fields = ['name', 'in_stock']
    template_name = "inventory_create.html"
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        
        return HttpResponseRedirect('/inventory')

class Inventory_Detail(DetailView):
    model = Inventory
    template_name = "inventory_detail.html"

    
@method_decorator(login_required, name="dispatch")
class Inventory_Update(UpdateView):
    model = Inventory
    fields = ['name', 'in_stock', 'devices']
    template_name = 'inventory_update.html'
    # success_url = "/inventory"
    # def form_valid(self,form):
    #     print(self.object.in_stock)
    def get_success_url(self):
        return reverse('inventory_detail', kwargs={'pk': self.object.pk})
    
    
# @method_decorator(login_required, name="dispatch")
# class Inventory_Update(UpdateView):
#     model = Inventory
#     fields = ['name']
#     template_name = 'inventory_update.html'
#     success_url = "/inventory"
    
@method_decorator(login_required, name="dispatch")    
class Inventory_Add(UpdateView):
    model = Inventory
    fields = ["add"]
    template_name = 'inventory_add.html'
    success_url = "/inventory"
    inventory = Inventory.objects.all()
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        add = self.object.add
        print(self.object.name)
        if self.object.name == self.object.name:
            inventory_stock = Inventory.objects.filter(name=f'{self.object.name}')
            inventory_stock.update(in_stock=F('in_stock') + add)     
            
        
        return HttpResponseRedirect('/inventory')
    
@method_decorator(login_required, name="dispatch")
class Inventory_Delete(DeleteView):
    model = Inventory
    template_name = 'inventory_delete.html'
    success_url = '/inventory'
   
###########################SIGNUP##################################

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse('/user/'+str(user))
        else:
            return render(request,'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    
    
