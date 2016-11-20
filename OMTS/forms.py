from django import forms
from django.forms import ModelForm
from OMTS.models import studentInfo
from django.utils.safestring import mark_safe

class ContactForm(forms.Form):
        ECSU_email = forms.EmailField(required=True)
        
class emailStudent(ModelForm):
    class Meta:
        model = studentInfo
        fields = ['studentEmail']
