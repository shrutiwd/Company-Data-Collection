from django.contrib import admin
from django.urls import path
from . import views

app_name = 'company_data'

urlpatterns = [

    path('', views.company_details, name='company_details'),
    path('company-details/', views.show, name='show'),
]
