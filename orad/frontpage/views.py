from django.shortcuts import render
from django.urls import path
from .form import Newfile


# Create your views here.

def front(request):
    return render(request, 'frontpage/index.html')

def page(request):
    form = Newfile()

    if request.method == "POST":
        form = Newfile(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return front(request)
    return render(request, 'frontpage/frontpage.html', {'form':form})