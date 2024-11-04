from django.shortcuts import render,redirect
from .forms import register_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
# Create your views here.
def home(request):
    return render(request,'base.html')
def sign_up(request):
    if request.method=="POST":
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form=register_form()
    return render(request,'register.html',{'form':form})

def signin(request):
    if request.method=="POST":
        form =AuthenticationForm(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                return redirect('login')
    form =AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('login')