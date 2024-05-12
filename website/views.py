from django.shortcuts import render
from website.models import Contact
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import NameForm, ContactForm, NewsletterForm



def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        request.POST._mutable = True
        request.POST['name'] = 'Anonymous'
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR,'your ticket  did not submited successfully')

    form = ContactForm()   
    return render(request, 'website/contact.html', {"form":form})


def newsletter_view(request):
    if request.method =="POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")

def test_view(request):
    if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("done")
            else:
                return HttpResponse("not valid")
            
    form = ContactForm()
    return render(request, 'test.html', {'form': form})

