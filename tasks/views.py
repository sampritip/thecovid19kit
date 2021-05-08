from django.shortcuts import render
from django.http import HttpResponse
from .models import Post1

# Create your views here.
def index(request):
           return render(request, 'tasks/home.html')
def need(request):
    posts = Post1.objects.all()
    return render(request, 'tasks/need.html', {'posts':posts})


def give(request):
    return render(request, 'tasks/give.html')