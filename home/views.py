from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from .forms import ContactForm
from .models import Contact, Project

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           contact = Contact()
           contact.name = request.POST.get('name')
           contact.email = request.POST.get('email')
           contact.subject = request.POST.get('subject')
           contact.desc = request.POST.get('desc')
           contact.save()
           
    else:
        form = ContactForm()
    
    project_all = Project.objects.all()
    return render(request,  "home/index.html", {'form': form, 'project':project_all})
    
 