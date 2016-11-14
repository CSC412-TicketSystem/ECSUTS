from django.shortcuts import render, redirect, render_to_response
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from AppTicket.forms import ContactForm
from django.template import RequestContext

# Create your views here.
def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            to_email = form.cleaned_data['ECSU_email']
            subject = 'Testin'
            message = 'Fill out the form at 127.0.0.1:8000/Contact'
            email = 'ECSU_Maintenance@ecsu.edu'

            if '@' in to_email and not to_email.endswith('@students.ecsu.edu'):
                return HttpResponse('That is not a valid Email')
            try:
                send_mail(subject, message, email , [to_email])
            except BadHeaderError:

                return HttpResponse('Invalid Header found.')

            return redirect('thanks')

    return render(request, 'test.html', {'form': form,})

def thanks(request):
    return HttpResponse('Check Your Email')

def Contact(request):
    return render(request, 'DanielForm.html')
