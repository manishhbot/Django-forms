from django.shortcuts import render
from .test_forms import First_form 

# Create your views here.

def welcome(request):
    return render(request, 'firstform/index.html')

def formm(request):
    form = First_form()

    if request.method == 'POST':
        form = First_form(request.POST)
        if form.is_valid():
            print('validation')
            print(form.cleaned_data['name'])

    return render(request, 'firstform/form.html', {'form':form})