from django.forms import ModelForm, TextInput, Textarea, EmailInput, Select
from . import models
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = models.contactFormMessage
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your message here', 'rows': '6'}),
            
        }

class FreeWebsiteForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = models.freeWebsiteLead
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'whatsapp_number', 'details']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'whatsapp_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Whatsapp number'}),
            'details': Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell me a little bit about the website you want', 'rows': '6'}),
            
        }


class QuotationForm(ModelForm):
    class Meta:
        model = models.Quotation
        fields = ['full_name', 'email', 'phone_number', 'country', 'notes']
        widgets = {
            'full_name': TextInput(attrs={'class': 'full-input', 'placeholder': 'Type your first name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Type your email here'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your phone number'}),
            'country': TextInput(attrs={'class': 'full-input', 'placeholder': 'Type your Country'}),
            'notes': Textarea(attrs={'class': 'full-input', 'placeholder': 'Any information that think can help me undestand the website you need?', 'rows': '6'}),
        }

class specialOfferLeadsForm(ModelForm):
    class Meta:
        model = models.specialOfferLeads
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'website_details']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}),
            'website_details': Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell me about the website you want'}),
        }