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
        
class studentIssueForm(forms.Form):
    #full_Name = forms.CharField(max_length=150)
    
    class Meta: 
        model = studentInfo
        exclude = ['studentEmail']
        widgets = {
            'residence_Hall':forms.Select(),
            'occupancy':forms.RadioSelect(),
            'issues':forms.Select(),
            'rank_Of_Ticket':forms.Select(),
        }
    
    
    