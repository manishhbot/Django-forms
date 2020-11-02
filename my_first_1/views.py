from django.shortcuts import render
from django.urls import path

# Create your views here.

def help(request):
    mydict = {'insert_me': 'This line is from view'}
    return render(request, 'first_app_1/help.html', context = mydict)

