from django.shortcuts import render
from django.http import HttpResponse
from home.models import NewsLetter
import json
import re

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')

def tandc(request):
    return render(request, 'home/termandconditions.html')

def privacy(request):
    return render(request, 'home/privacy.html')

def email_list(request):
    if request.method == 'POST':

        email = request.POST["email"]

        if(email != "" and re.match(r"[^@]+@[^@]+\.[^@]+", email)):

            NewsLetter.objects.create (
                email = email
            )

            return HttpResponse('')

        else:
            
            return HttpResponse('Invalid Email')
