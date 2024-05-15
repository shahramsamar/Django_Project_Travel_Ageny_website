from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request,"coming_soon.html")