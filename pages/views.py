from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'about.html'

class HomePageView(TemplateView):
    template_name = 'home.html'
# Create your views here.

def somePage(request):
    return HttpResponse('hello')