from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    #Employees
    path('employees/', views.Employee_List.as_view(), name="employee_list"),
     #Devices
    path('employees/devices/', views.Device_List.as_view(), name="device_list"),
    #auth
    #  path('user/<username>', views.profile, name='employee'),
    path('accounts/signup/', views.signup_view, name='signup')


    
]