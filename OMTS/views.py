from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import studentInfo
#from .models import studentInfo, studentTicket

# Create your views here.

def index(request):
    
    
    template = loader.get_template('OMTS/test.html')
    return HttpResponse(template.render(request))
 

def begform(request):
    template = loader.get_template('OMTS/')