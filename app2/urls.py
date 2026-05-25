from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
          # 👈 home page
    path('aman/', views.amanu),     # 👈 dk page
    path('anshu/',views.anshui),
]