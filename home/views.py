from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')

def tandc(request):
    return render(request, 'home/termandconditions.html')

def privacy(request):
    return render(request, 'home/privacy.html')
