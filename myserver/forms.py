# forms.py
from django import forms
from .models import FormSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ['name', 'email', 'message']
