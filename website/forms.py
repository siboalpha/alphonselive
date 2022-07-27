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

class QuotationForm(ModelForm):
    class Meta:
        model = models.Quotation
        fields = ['first_name', 'last_name', 'email', 'phone_number', 
        'website_type', 'domain_name', 'hosting', 'web_design', 
        'web_development', 'seo', 'technical_suport', 'notes']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Type your email here'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your phone number'}),
            'website_type': Select(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'domain_name': Select(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'hosting': Select(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'web_design': Select(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'web_development': Select(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'seo': Select(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'technical_suport': Select(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'notes': Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your message here', 'rows': '6'}),
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