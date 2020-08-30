from django.shortcuts import render


def index(request):
    return render(request, 'frontend/home/home.html')

def login(request):
    return render(request, 'frontend/login/login.html')

def signup(request):
    return render(request, 'frontend/signup/signup.html')    

def aboutUs(request):
    return render(request, 'frontend/aboutUs/aboutUs.html')

def dashboard(request):
    return render(request,'frontend/dashboard/dashboard.html')