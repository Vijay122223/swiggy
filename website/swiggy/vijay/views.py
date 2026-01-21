from django.shortcuts import render
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request,'home.html')
def menu(request):
    return render(request,'menu.html')
def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        username=request.POST.get('username')
        User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("signin")
        messages.success(request,'User Created Successfully! Please signin to continue')
        return redirect('signin')
    return render(request,'signup.html')

from django.contrib.auth import authenticate,login
def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login Success')
            return redirect('menu')
        messages.error(request,'Invalid Credentials, Try Again!')
        return render(request,'signin.html')
    return render(request,'signin.html')