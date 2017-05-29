from django.shortcuts import render

# Create your views here.
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^contact/', views.contact),
    url(r'^about/', views.about),
    url(r'^profile/', views.profile)
]
