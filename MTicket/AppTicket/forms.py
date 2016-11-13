from django import forms
from django.utils.safestring import mark_safe

class ContactForm(forms.Form):
    ECSU_email = forms.EmailField(required=True)

