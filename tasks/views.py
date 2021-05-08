from django.shortcuts import render
from django.http import HttpResponse
from .models import Post1,Post2
from .forms import Request,Supply

# Create your views here.
def index(request):
           return render(request, 'tasks/home.html')
def need(request):
    posts = Post1.objects.all()
    return render(request, 'tasks/need.html', {'posts':posts})

def give(request):
    posts = Post2.objects.all()
    return render(request, 'tasks/give.html', {'posts':posts})



def add_request(request):
    form = Request()
    if request.method == 'POST':
        form = Request(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tasks/add_request.html',{'form':form})

def add_supply(request):
    form = Supply()
    if request.method == 'POST':
        form = Request(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tasks/add_supply.html',{'form':form})


    