from distutils.command.upload import upload
from email import message
from django.db import models
from django.forms import model_to_dict
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class contactFormMessage(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=40)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name

class specialOfferLeads(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=40)
    industry = models.CharField(max_length=40)
    website_details = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name

class Quotation(models.Model):
    basic_website = 'Basic Website'
    standard_website = 'Standard Website'
    advanced_website = 'Advanced Website'

    WEBSITE_TYPE_CHOICES = [
        (basic_website, 'Basic Website'),
        (standard_website, 'Standard Website'),
        (advanced_website, 'Advanced Website'),
    ]

    Yes = 'Yes'
    No = 'No'

    YES_OR_NO_QUESTION_CHOICES = [
        (Yes, 'Yes'),
        (No, 'No'),
    ]
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    website_type = models.CharField(max_length=40, choices=WEBSITE_TYPE_CHOICES, default=basic_website)
    domain_name = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    domain_name_value = models.CharField(max_length=40, default=0)
    hosting = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    hosting_value = models.CharField(max_length=40, default=0)
    web_design = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    web_design_value = models.CharField(max_length=40, default=0)
    web_development = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    web_development_value = models.CharField(max_length=40, default=0)
    technical_suport = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    technical_suport_value = models.CharField(max_length=40, default=0)
    seo = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    seo_value = models.CharField(max_length=40, default=0)
    notes = models.TextField(max_length=1000, null=True, blank=True)
    quotation_total = models.CharField(max_length=40, default=0)

    def __str__(self):
        return self.first_name

class Project (models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to = 'Projects Images')
    project_image_mobile = models.ImageField(upload_to = 'Projects Images', null=True)
    started_on = models.DateField(auto_now_add=None)
    completed_on = models.DateField(auto_now_add=None)
    details = models.TextField(max_length=2500)
