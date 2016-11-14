from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('MaintTick/Nigel2Page.html', context)

def Daniel(request):
   return render(request, 'MaintTick/DanielForm.html')

