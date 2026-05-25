from django.contrib import admin
from django.urls import path
from app1 import views   # import your views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  
    path('am/',views.about),
    path('as/',views.contact),
    path('dk/', views.dk),     # 👈 dk page
]