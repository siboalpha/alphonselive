import email
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

from website.models import Quotation, Project
from .forms import ContactForm, QuotationForm
from django.core.mail import EmailMessage
from core import settings
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    projects = Project.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            client_name = form.cleaned_data['first_name']
            client_email = form.cleaned_data['email']
            context = {'client_name': client_name, 'client_email': client_email}
            email_template = render_to_string('emails/new_lead.html', context)

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
    context = {'form': form, 'projects':projects}
    return render(request, 'index.html', context)

def offer(request):
    return render(request, 'offer.html')

def thankYou(request):
    return render(request, 'thank-you.html')


def quotation(request):
    form = QuotationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            website_category_input = form.cleaned_data['website_type']
            if website_category_input == 'Basic Website':
                hosting_value = 60
                domain_name_value = 12
                web_design_value = 50
                web_development_value = 200
                seo_value = 0
                technical_suport_value = 0

                if form.cleaned_data['hosting'] == 'Yes':
                    hosting_value = 0
                if form.cleaned_data['domain_name'] == 'Yes':
                    domain_name_value = 0
                if form.cleaned_data['web_design'] == 'Yes':
                    web_design_value = 0
                if form.cleaned_data['web_development'] == 'Yes':
                    web_development_value = 0
                if form.cleaned_data['technical_suport'] == 'Yes':
                    technical_suport_value = 12
                if form.cleaned_data['seo'] == 'Yes':
                    seo_value = 100


            elif website_category_input == 'Standard Website':
                hosting_value = 40
                domain_name_value = 20
                web_design_value = 150
                web_development_value = 300
                seo_value = 0
                technical_suport_value = 0

                if form.cleaned_data['hosting'] == 'Yes':
                    hosting_value = 0
                if form.cleaned_data['domain_name'] == 'Yes':
                    domain_name_value = 0
                if form.cleaned_data['web_design'] == 'Yes':
                    web_design_value = 0
                if form.cleaned_data['web_development'] == 'Yes':
                    web_development_value = 0
                if form.cleaned_data['technical_suport'] == 'Yes':
                    technical_suport_value = 112
                if form.cleaned_data['seo'] == 'Yes':
                    seo_value = 200


            elif website_category_input == 'Advanced Website':
                hosting_value = 300
                domain_name_value = 100
                web_design_value = 350
                web_development_value = 900
                seo_value = 0
                technical_suport_value = 0
            
                if form.cleaned_data['hosting'] == 'Yes':
                    hosting_value = 0
                if form.cleaned_data['domain_name'] == 'Yes':
                    domain_name_value = 0
                if form.cleaned_data['web_design'] == 'Yes':
                    web_design_value = 0
                if form.cleaned_data['web_development'] == 'Yes':
                    web_development_value = 0
                if form.cleaned_data['technical_suport'] == 'Yes':
                    technical_suport_value = 212
                if form.cleaned_data['seo'] == 'Yes':
                    seo_value = 400
            else: 
                total = 0

            total = hosting_value + domain_name_value + web_design_value + web_development_value + seo_value + technical_suport_value
            domain_name = form.save(commit=False)
            domain_name.domain_name_value = domain_name_value

            hosting = form.save(commit=False)
            hosting.hosting_value = hosting_value

            web_design = form.save(commit=False)
            web_design.web_design_value = web_design_value

            web_development = form.save(commit=False)
            web_development.web_development_value = web_development_value

            seo = form.save(commit=False)
            seo.seo_value = seo_value

            technical_suport = form.save(commit=False)
            technical_suport.technical_suport_value = technical_suport_value
            
            form_total = form.save(commit=False)
            form_total.quotation_total = total
            form.save()
            instance = form.save()
            return redirect('quotation-results', pk=instance.pk)
    return render(request, 'quotation.html', context)

def quotationResults(request, pk):
    quotation = Quotation.objects.get(id=pk)
    context = {'quotation': quotation}
    return render(request, 'quotation-results.html', context)

def singlePortfolio(request,pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'single-portfolio.html', context)