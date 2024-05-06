from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from accounts.forms import Signup

from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin



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
                    messages.success(request,"Login successfully")
                    if user is not None:
                        login(request,user)
                        return redirect("/") 
                else:
                    messages.error(request,'Invalid credentials, Please check username/email or password. ')
    
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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('/')