from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import User, Device, Employee
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(TemplateView):
    template_name='home.html'
 
class About(TemplateView):
    template_name='about.html'


class Employee_Create(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['first name', 'last name', 'Department', 'Devices', ]
    template_name = "employee_create.html"
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponse('/users')

class Employee_List(TemplateView):
    template_name='employee_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        
        if name != None:
            context['employees']=Employee.objects.filter(name__icontains=name)
            context['header']= f'Searching for {name}'
        else:
            context['employees']=Employee.objects.all()
            context['devices']=Device.objects.all()
            context['header']= 'Employees:'
            
        return context
    
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
def profile(request, username):
    user = User.objects.get(username=username)
    devices = Device.objects.filter(user=user)
    employees = Employee.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'devices': devices, 'employees':employees})




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
    
    
