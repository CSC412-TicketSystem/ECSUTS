from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage' : "I am bold front"}
    return render_to_response('MaintTick/index.html', context_dict,context)
