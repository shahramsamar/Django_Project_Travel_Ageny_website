from django.shortcuts import render
from website.models import Contact
from django.http import HttpResponse
from website.forms import NameForm



def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    return render(request, 'website/contact.html')

def test_view(request):
    if request.method == "POST":
            form = NameForm(request.POST)
            if form.is_valid():
                name = form.changed_data['name']
                email = form.changed_data['email']
                subject = form.changed_data['subject']
                message = form.changed_data['message']
                print(name, email, subject, message)
                return HttpResponse("done")
            else:
                return HttpResponse("not valid")
            

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
    form = NameForm()
    return render(request, 'test.html', {'form': form})
