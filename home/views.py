from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    http_method_names = ['get']
    template_name = "home/index.html"
    