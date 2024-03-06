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
        contact = Contact()
        if form.is_valid():
 
            contact.name ='unknown'
            contact.email = request.POST.get('email')
            contact.subject = request.POST.get('subject')
            contact.message = request.POST.get('message')
            
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            # print(name, email, subject, message)
            # form.save()
            contact.save()
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
                # name = form.cleaned_data['name']
                # email = form.cleaned_data['email']
                # subject = form.cleaned_data['subject']
                # message = form.cleaned_data['message']
                # print(name, email, subject, message)
                form.save()
                return HttpResponse("done")
            else:
                return HttpResponse("not valid")
            
    form = ContactForm()
    return render(request, 'test.html', {'form': form})

    #  name = request.POST.get('name')
    #  print(name)
    #  email = request.POST.get('email')
    #  subject = request.POST.get('subject')
    #  message = request.POST.get('message')
    #  contact = Contact()
    #  contact.name = name
    #  contact.email = email
    #  contact.subject = subject
    #  contact.message = message 
    #  contact.save()
    #  print(name, email ,subject, message)
