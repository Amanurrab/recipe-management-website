from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponse
from datetime import datetime
def home(request):
    peoples=[
        {"name":"amanurrab","age":16},
        {"name":"anshukumar khanna","age":77},
        {"name":"rijwan ansari","age":90}



    ]

    vegetables=["potato","tomato","cucumber","aaaluu"]

    text="qqqqqqqqqqqqqqqqqqqqqqqqqsqqqqqqqqqqqqqqqqqqqqqqwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwweeeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrttttttttttttyyyyyyyyyyyuuuuuuuuuuiiiiiii"
   
    return render(request,"app1/index.html",context={'peoples':peoples,'datetimes':datetime.now(),'texta':text,'vegetables':vegetables})

def dk(request):
    return HttpResponse("HELLO ALL DJANGO USER ALL WELCOME YOU")


def about(request):
    # yaha per jo likhenge av wo website ka upper m aayega likhaa huwa
    
    return render(request,"app1/about.html",{'page': 'about Page'})

def contact(request):
    context={'page':'contact hai mera'}
    return render(request,"app1/contact.html",{'page': 'Contact Page'})