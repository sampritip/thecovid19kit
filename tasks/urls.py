from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('home', views.index, name = "home"),
    path('need', views.need , name= "need"),
    path('give', views.give, name= "give"),
]
