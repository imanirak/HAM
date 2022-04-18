from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    #auth
    #  path('user/<username>', views.profile, name='employee'),
    path('accounts/signup/', views.signup_view, name='signup')


    
]