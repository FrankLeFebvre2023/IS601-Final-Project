from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def storeHome(request):
    template = loader.get_template("storeHome.html")
    return HttpResponse(template.render())