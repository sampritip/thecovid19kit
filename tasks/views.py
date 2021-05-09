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

def login(request):
    return render(request, 'tasks/login.html')

def loginpage(request):
    return render(request, 'account/login.html')

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
        form = Supply(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tasks/add_supply.html',{'form':form})


def technical_404_response(request, exception):
    """Create a technical 404 error response. `exception` is the Http404."""
    try:
        error_url = exception.args[0]['path']
    except (IndexError, TypeError, KeyError):
        error_url = request.path_info[1:]  # Trim leading slash

    try:
        tried = exception.args[0]['tried']
    except (IndexError, TypeError, KeyError):
        tried = []
    else:
        if (not tried or (                  # empty URLconf
            request.path == '/' and
            len(tried) == 1 and             # default URLconf
            len(tried[0]) == 1 and
            getattr(tried[0][0], 'app_name', '') == getattr(tried[0][0], 'namespace', '') == 'admin'
        )):
            return default_urlconf(request)
    
def default_urlconf(request):
    """Create an empty URLconf 404 error response."""
    with Path(CURRENT_DIR, 'tasks', 'login.html').open() as fh:
        t = DEBUG_ENGINE.from_string(fh.read())
    c = Context({
        'version': get_docs_version(),
    })

    return render(request, 'tasks/login.html')