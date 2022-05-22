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
