from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
                        return redirect("/")
        
            form = AuthenticationForm()     
            context = {"form":form}   
            return render(request,'accounts/login.html',context)
        else:
            return redirect("/")

@login_required
def logout_views(request):
        logout(request)
        return redirect("/")


# def signup_views(request):
    
#     return render(request, 'accounts/signup.html')


# def forgot_password_views(request):
    
#     return render(request, 'accounts/forgot_password.html')

