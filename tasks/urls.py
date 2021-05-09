from . import views
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.login, name="loginL"),
    path('login/home', views.index, name = "home"),
    path('need', views.need , name= "need"),
    path('give', views.give, name= "give"),
    path('need/add_request', views.add_request, name= "add_request"),
    path('give/add_supply', views.add_supply, name= "add_supply"),
    path('login', views.loginpage, name= "login"),
    
   
    
   
   

]
