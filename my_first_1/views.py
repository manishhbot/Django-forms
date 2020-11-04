from django.shortcuts import render
from django.urls import path
from my_first_1.models import Freedemo, Onboarded, Registrations

# Create your views here.

def level_up(request):
    new_var = Freedemo.objects.order_by('name')
    mydict = {'free_demo': new_var}
    return render(request, 'my_first_1/model_2.html', context = mydict)

