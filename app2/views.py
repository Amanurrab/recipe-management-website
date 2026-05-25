from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



def amanu(request):
    return HttpResponse("HELLO ALL DJANGO USER ALL WELCOME YOU amanuurab")


def anshui(request):
    return HttpResponse('<h1>hello world</h1>')