from django.db import models
from django.utils import timezone
# Create your models here.

class contactFormMessage(models.Model):
    date_sent = models.DateTimeField(default=timezone.now, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=40)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name

class freeWebsiteLead(models.Model):
    contacted = 'Contacted'
    not_contacted = 'Not contacted'
    not_paid = 'Not paid'
    payment_pending = 'Payment_pending'

    STATUS_CHOICES = [
        (contacted, 'Contacted'),
        (not_contacted, 'Not contacted'),
        (not_paid, 'Not paid'),
        (payment_pending, 'Payment_pending'),
    ]
    date_sent = models.DateTimeField(default=timezone.now, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=40)
    whatsapp_number = models.CharField(max_length=40, null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=not_contacted, null=True)
    details = models.TextField(max_length=500)


    def __str__(self):
        return self.first_name

class specialOfferLeads(models.Model):
    date_sent = models.DateTimeField(default=timezone.now, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=40)
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
    date_sent = models.DateTimeField(default=timezone.now, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    country = models.CharField(max_length=40, null=True)
    website_type = models.CharField(max_length=40, null=True, choices=WEBSITE_TYPE_CHOICES, default=basic_website)
    domain_name = models.CharField(max_length=40, null=True, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    domain_name_value = models.CharField(max_length=40, null=True, default=0)
    hosting = models.CharField(max_length=40, null=True, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    hosting_value = models.CharField(max_length=40, null=True, default=0)
    web_design = models.CharField(max_length=40, null=True, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    web_design_value = models.CharField(max_length=40, null=True, default=0)
    web_development = models.CharField(max_length=40, null=True, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    web_development_value = models.CharField(max_length=40, null=True, default=0)
    technical_suport = models.CharField(max_length=40, null=True, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    technical_suport_value = models.CharField(max_length=40, null=True, default=0)
    seo = models.CharField(max_length=40, null=True, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    seo_value = models.CharField(max_length=40, null=True, default=0)
    notes = models.TextField(max_length=1000, null=True, blank=True)
    quotation_total = models.CharField(max_length=40, null=True, default=0)

    def __str__(self):
        return self.first_name

class Project (models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to = 'Projects Images')
    project_image_mobile = models.ImageField(upload_to = 'Projects Images', null=True)
    started_on = models.DateField(auto_now_add=None)
    completed_on = models.DateField(auto_now_add=None)
    details = models.TextField(max_length=2500, null=True)

    def __str__(self):
        return self.title

    def short_description(self):
        return self.details[0:100] + "..."

    class Meta:
        ordering = ['id']
