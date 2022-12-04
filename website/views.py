from django.http import HttpResponse
from django.shortcuts import redirect, render

from website.models import Quotation, Project
from .forms import ContactForm, FreeWebsiteForm, QuotationForm, specialOfferLeadsForm
from django.core.mail import EmailMessage
from core import settings
from django.template.loader import render_to_string

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    all_projects = Project.objects.order_by("-completed_on")
    paginaginated_projects = Paginator(all_projects, 8, allow_empty_first_page=True)
    page_number = request.GET.get('page')
    projects = paginaginated_projects.get_page(page_number)
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            '''
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
            '''
            return redirect('thank-you')
    context = {'form': form, 'projects':projects}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    my_projects = Project.objects.all()

    context = {'my_projects':my_projects}
    return render(request, 'projects.html', context)

def project(request, slug):
    my_project = Project.objects.get(slug = slug)
    context = {'my_project':my_project}
    return render(request, 'project.html', context)

def offer(request):
    form = FreeWebsiteForm()
    context = {'form': form}
    if request.method == 'POST':
        form = FreeWebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
        else:
            return HttpResponse('There was an error')
    return render(request, 'offer.html', context)

def offer500(request):
    form = QuotationForm()
    context = {'form': form}
    return render(request, '500-website.html', context)

def thankYou(request):
    return render(request, 'thank-you.html')


def quotationUpdate(request,pk):
    form = QuotationForm()
    quotation = Quotation.objects.get(id=pk)
    context = {'form': form}
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
            instance = form.save()
            return redirect('quotation-results.html', pk = instance)
        else:
            return HttpResponse('There was an error')
    return render(request, 'quotation-update.html', context)

def thankYou(request):
    return render(request, 'thank-you.html')


def quotation(request):
    form = QuotationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    return render(request, 'quotation.html', context)

def quotationResults(request, pk):
    quotation = Quotation.objects.get(id=pk)
    context = {'quotation': quotation}
    return render(request, 'quotation-results.html', context)

def singlePortfolio(request,pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'single-portfolio.html', context)
