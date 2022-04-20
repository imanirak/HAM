from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    #Employees
    path('employees/new', views.Employee_Create.as_view(), name="employee_create"),
    path('employees/', views.Employee_List.as_view(), name="employee_list"),
     path('employees/<int:pk>/', views.Employee_Detail.as_view(), name="employee_detail"),
    path('employees/<int:pk>/update', views.Employee_Update.as_view(), name="employee_update"),
    path('employees/<int:pk>/delete', views.Employee_Delete.as_view(), name="employee_delete"),
    
     #Devices
    path('devices/', views.devices_index, name="devices_index"),
    path('devices/<int:device_id>', views.devices_show, name='devices_show'),
    path('devices/new', views.Device_Create.as_view(), name="device_create"),
    path('devices/<int:pk>/update', views.Device_Update.as_view(), name="devices_update"),
    path('devices/<int:pk>/delete', views.Device_Delete.as_view(), name="devices_delete"),
    
    
    #auth
    #  path('user/<username>', views.profile, name='employee'),
    path('accounts/signup/', views.signup_view, name='signup')


    
]