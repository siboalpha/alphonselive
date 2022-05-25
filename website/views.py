import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ContactForm, QuotationForm
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


def quotation(request):
    form = QuotationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            website_category_input = form.cleaned_data['website_type']
            if website_category_input == 'Basic Website':
                hosting = 60
                domain_name = 20
                web_design = 100
                web_development = 200
                seo = 0
                technical_suport = 12

                print (website_category_input)
                if form.cleaned_data['hosting'] == 'Yes':
                    hosting = 0
                if form.cleaned_data['domain_name'] == 'Yes':
                    domain_name = 0
                if form.cleaned_data['web_design'] == 'Yes':
                    web_design = 0
                if form.cleaned_data['web_development'] == 'Yes':
                    web_development = 0
                if form.cleaned_data['technical_suport'] == 'Yes':
                    technical_suport = 0
                if form.cleaned_data['seo'] == 'Yes':
                    seo == 100

                total = hosting + domain_name + web_design + web_development + seo + technical_suport
                print(total)

            elif website_category_input == 'Standard Website':
                hosting = 100
                domain_name = 20
                web_design = 300
                web_development = 600
                seo = 0
                technical_suport = 0

                print (website_category_input)
                if form.cleaned_data['hosting'] == 'Yes':
                    hosting = 0
                if form.cleaned_data['domain_name'] == 'Yes':
                    domain_name = 0
                if form.cleaned_data['web_design'] == 'Yes':
                    web_design = 0
                if form.cleaned_data['web_development'] == 'Yes':
                    web_development = 0
                if form.cleaned_data['technical_suport'] == 'Yes':
                    technical_suport = 50
                if form.cleaned_data['seo'] == 'Yes':
                    seo == 200

                total = hosting + domain_name + web_design + web_development + seo + technical_suport
                print(total)

            elif website_category_input == 'Advanced Website':
                hosting = 300
                domain_name = 50
                web_design = 500
                web_development = 1600
                seo = 0
                technical_suport = 0

                print (website_category_input)
                if form.cleaned_data['hosting'] == 'Yes':
                    hosting = 0
                if form.cleaned_data['domain_name'] == 'Yes':
                    domain_name = 0
                if form.cleaned_data['web_design'] == 'Yes':
                    web_design = 0
                if form.cleaned_data['web_development'] == 'Yes':
                    web_development = 0
                if form.cleaned_data['technical_suport'] == 'Yes':
                    technical_suport = 150
                if form.cleaned_data['seo'] == 'Yes':
                    seo == 300

                total = hosting + domain_name + web_design + web_development + seo + technical_suport
                print(total)
            else: 
                total = 0

    return render(request, 'website/quotation.html', context)