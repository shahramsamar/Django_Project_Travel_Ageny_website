from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(requests):
    # return HttpResponse("hello shari")
    # return HttpResponse('<h1>Home page</h1>')
    return render(requests,'website/index.html')

def about_view(requests):
    # return HttpResponse('<h1>About page</h1>')
    return render(requests,'website/about.html')

def contact_view(requests):
    # return HttpResponse('<h1>Contact page</h1>')
    # return render(requests,'contact.html')
    return render(requests,'website/contact.html')

