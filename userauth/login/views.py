from django.shortcuts import render
from .form import Admin, Detailss, Djangouserr

#imports related to login and logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_d = Admin(data=request.POST)
        picture_d = Djangouserr(data=request.POST)

        if user_d.is_valid() and picture_d.is_valid():
            user = user_d.save()
            user.set_password(user.password)
            user.save()

            picturee = picture_d.save(commit=False)
            picturee.user = user

            if 'picture' in request.FILES:
                picturee.picture = request.FILES['picture']

            picturee.save()

            registered = True

        else:
            print(user_d.errors, picture_d.errors)
    else:
        user_d = Admin()
        picture_d = Djangouserr()
    return render(request, 'register.html',
                  {'user_d': user_d, 'picture_d': picture_d, 'registered': registered})


def detailsss(request):
    abc = Detailss

    if request.method == 'POST':
        abc = Detailss(request.POST)
        if abc.is_valid():
            abc.save(commit=True)
    return render(request, 'index.html', {'abc': abc})
