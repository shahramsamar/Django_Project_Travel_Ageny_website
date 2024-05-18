from django.shortcuts import render

# Create your views here.
def coming_soon(request,*args, **kwargs):
    return render(request,"coming_soon.html")