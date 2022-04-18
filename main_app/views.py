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


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    devices = Device.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'devices': devices})


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
    
    
