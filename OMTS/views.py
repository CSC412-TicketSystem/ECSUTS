#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader

#from .models import studentInfo
#from .models import studentInfo, studentTicket

# Create your views here.

#def index(request):
    #template = loader.get_template('OMTS/test.html')
    #return HttpResponse(template.render(request))

#def begform(request):
    #template = loader.get_template('OMTS/')
    
from django.shortcuts import render, redirect, render_to_response
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from OMTS.forms import ContactForm, studentIssueForm
from django.template import RequestContext
from django.utils import timezone
from .models import studentInfo #studentTicket

# Create your views here.
def email(request):
    if request.method == 'GET':
        #form = emailStudent()
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            to_email = form.cleaned_data['ECSU_email']
            str_to_email = str(to_email)
            subject = 'ECSU Maintanence Ticket System'
            message = 'Dear Student, Welcome to ECSU Maintenance Ticket System.  In order to begin filing your maintenance issue, please copy and paste the URL into your web browser.  127.0.0.1:8000/Contact'
            email = 'ecsumaintenancesystem@gmail.com'
            
            ############### new code #################
            #newForm = emailStudent(request.POST)
            #model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            #model_instance.save()
            
            student_email = studentInfo(studentEmail = str_to_email)
            student_email.save()
            ###########################################
            
            if '@' in to_email and not to_email.endswith('@students.ecsu.edu'):
                return HttpResponse('That is not a valid Email')
            try:
                send_mail(subject, message, email , [to_email])
            except BadHeaderError:

                return HttpResponse('Invalid Header found.')

            #return redirect('thanks')

    return render(request, 'OMTS/jeff_t3.html', {'form': form,})
    # 'OMTS/test.html' -> put this back if it doesn't work, but it is not using jeff_t3.html that is a copy of Odell's html form
    

def thanks(request):
    return HttpResponse('Check Your Email')


def Contact(request):
     ############### new code #################
    if request.method == 'GET':
        #form = emailStudent()
        form = studentIssueForm()
    else:
        form = studentIssueForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['student_name']
            resid_hall = form.cleaned_data['resid_hall']
            room_num = form.cleaned_data['room_num']
            occupancy = form.cleaned_data['occupancy']
            issues = form.cleaned_data['issues']
            rankOfTicket = form.cleaned_data['rankOfTicket']
            briefDescription = form.cleaned_data['briefDescription']
            
            
            #str_to_name = str(name)
            
           
            student_Info = studentInfo(name, resid_hall, room_num, occupancy, issues, rankOfTicket, briefDescription)
            student_Info.save()
            
           
            #if BadHeaderError:

                #return HttpResponse('Invalid Header found.')

            
        ###########################################
    return render(request, 'OMTS/jtest2.html', {'form':form,})