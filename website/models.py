from email import message
from django.db import models

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
        (basic_website, 'Web design'),
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
    hosting = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    web_design = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    web_development = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    technical_suport = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    seo = models.CharField(max_length=40, choices=YES_OR_NO_QUESTION_CHOICES, default=No)
    notes = models.TextField(max_length=1000, null=True, blank=True)
    quotation_total = models.CharField(max_length=40, default=0)
    