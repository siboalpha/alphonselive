import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ContactForm
from django.core.mail import EmailMessage
from core import settings
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            client_name = form.cleaned_data['first_name']
            client_email = form.cleaned_data['email']
            context = {'client_name': client_name, 'client_email': client_email}
            email_template = render_to_string('website/emails/new_lead.html', context)

            email = EmailMessage(
                'New Lead',
                email_template,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
            email.fail_silently = False
            try:
                email.send()
            except:
                return HttpResponse("Form saved but admin did not get an email")
            return redirect('thank-you')
    context = {'form': form}
    return render(request, 'website/index.html', context)

def offer(request):
    return render(request, 'website/offer.html')

def thankYou(request):
    return render(request, 'website/thank-you.html')
