from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from django.urls import clear_script_prefix
from . import models
# Register your models here.
@admin.register(models.contactFormMessage)
class contactFormMessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "date_sent")

@admin.register(models.freeWebsiteLead)
class freeWebsiteLeadLeadAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "date_sent", "status")

@admin.register(models.Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "website_type", "quotation_total", "date_sent")


@admin.register(models.Project)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "started_on", "completed_on")

@admin.register(models.specialOfferLeads)
class specialOfferLeadsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "date_sent")