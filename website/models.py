from django.db import models
from django.utils import timezone
from django.urls import reverse
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
    date_sent = models.DateTimeField(default=timezone.now, null=True)
    full_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    country = models.CharField(max_length=40, null=True)
    notes = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.first_name

class Project (models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, max_length=255)
    company = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to = 'Projects Images')
    project_image_mobile = models.ImageField(upload_to = 'Projects Images', null=True)
    started_on = models.DateField(auto_now_add=None)
    completed_on = models.DateField(auto_now_add=None)
    details = models.TextField(max_length=2500, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['id']
