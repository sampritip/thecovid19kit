from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('home', views.index, name = "home"),
    path('need', views.need , name= "need"),
    path('give', views.give, name= "give"),
    path('add_request', views.add_request, name= "add_request"),
    path('add_supply', views.add_supply, name= "add_supply"),

]
