from django.shortcuts import render
from . import views

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def signup(request):
    return render(request, 'app/signup.html')

def activity(request):
    return render(request, 'app/activity.html')

