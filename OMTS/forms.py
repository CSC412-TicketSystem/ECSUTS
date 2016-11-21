from django import forms
from django.forms import ModelForm
from OMTS.models import studentInfo
from django.utils.safestring import mark_safe
#(ModelForm):

class ContactForm(forms.Form):
    ECSU_email = forms.EmailField(required=True)
        
        #class Meta:
            #model = studentInfo
            #fields = ['studentEmail']
        
class studentIssueForm(ModelForm):
    class Meta: 
        model = studentInfo
        exclude = ['studentEmail']
    
    
    