from django.shortcuts import render
from .models import ContactDetails


# Create your views here.

def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST["Name"]
        email = request.POST["Email"]
        phone = request.POST["Phone"]
        company = request.POST["Company"]

        var = ContactDetails(Name=name, Email=email, Phone=phone, Company=company)
        var.save()

    return render(request, 'contact.html')


def tech1(request):
    return render(request, 'tech1.html')


def tech2(request):
    return render(request, 'tech2.html')


def tech3(request):
    return render(request, 'tech3.html')


def tech4(request):
    return render(request, 'tech4.html')


def tech5(request):
    return render(request, 'tech5.html')


def tech6(request):
    return render(request, 'tech6.html')
