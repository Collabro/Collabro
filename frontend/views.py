from django.shortcuts import render


def index(request):
    return render(request, 'frontend/home/home.html')

def login(request):
    return render(request, 'frontend/login/login.html')

def signup(request):
    return render(request, 'frontend/signup/signup.html')    
