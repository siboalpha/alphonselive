from django.forms import ModelForm, TextInput, Textarea, EmailInput
from . import models

class ContactForm(ModelForm):
    class Meta:
        model = models.contactFormMessage
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your message here', 'rows': '6'}),
        }