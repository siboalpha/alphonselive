from unicodedata import name
from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('offer/', views.offer, name='offer'),
    path('500-offer/', views.offer500, name='offer500'),
    path('thank-you/', views.thankYou, name='thank-you'),
    path('quotation/', views.quotation, name='quotation'),
    path('quotation-results/<pk>/', views.quotationResults, name='quotation-results'),
    path('quotation-update/<pk>/', views.quotationUpdate, name='quotation-update'),

    path('project/<pk>/', views.singlePortfolio, name='project'),
]