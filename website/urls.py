from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('offer/', views.offer, name='offer'),
]