from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from accounts.forms import Signup




# from django.http import HttpResponseRedirect
# Create your views here.
# def login_view(request):
    # if request.user.is_authenticated:
    #     msg = f"user is authenticated as {request.user.username}"
    # else:
    #    msg = "user is not authenticated"

    # if request.method =="POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    
def login_views(request):
        if not request.user.is_authenticated:
            if request.method == "POST":
                form = AuthenticationForm(request=request, data=request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')     
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request,user)
                        messages.success(request,"Login successfully")
                        return redirect("/") 
                else:
                    messages.error(request,'Invalid username/email or password, Please check username/email or password. ')
    
            form = AuthenticationForm()     
            context = {"form":form}   
            return render(request,'accounts/login.html',context)
        else:
            messages.error(request, 'you are logged in')
            return redirect("/")


@login_required
def logout_views(request):
        logout(request)
        messages.success(request,"Logout successfully")
        return redirect("/")


def signup_views(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
                form = Signup(request.POST)       
                if form.is_valid():
                    form.save()
                    messages.success(request,"User Create  successfully")
                    return redirect("/") 
                else:
                    messages.error(request, ' Failed User Created')

        form = Signup()     
        context = {"form":form}   
        return render(request,'accounts/signup.html',context)
    else:
        return redirect("/")


