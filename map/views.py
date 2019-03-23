from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request,'map/home.html',{})

def front(request):
	return render(request,'map/front.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('successfully loged in'))
            return redirect('home')
        else:
            messages.success(request,('please try again to loged in'))
            return redirect('login')
    else:
        return render(request,'map/login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,('logged out!!'))
    return render(request,'map/login.html',{})


def demo(request):
    return render(request,'map/demo.html')