from django.shortcuts import render
from .form import Newfile
from .models import Details


# Create your views here.

def front(request):
    forms = Details.objects.all()
    return render(request, 'frontpage/index.html', {'forms': forms})


def page(request):
    form = Newfile()

    if request.method == "POST":
        form = Newfile(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'frontpage/frontpage.html', {'form': form})


def relative(request):
    abc = 'Hello'
    abcd = 100
    return render(request, 'frontpage/relative.html', {'abc':abc, 'abcd':abcd})


def other(request):
    return render(request, 'frontpage/other.html')

