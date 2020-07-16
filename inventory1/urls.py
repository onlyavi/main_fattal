from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
 
  

    path('add_alchol_type/', add_alchol_type, name='add_alchol_type'),

]