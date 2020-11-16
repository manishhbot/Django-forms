from django.shortcuts import render, redirect
from .models import ContactDetails
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='Aman:login')
def home(request):
    return render(request, 'frontpage1/home.html')


def contact_d(request):
    if request.method == 'POST':
        name = request.POST["Name"]
        email = request.POST["Email"]
        phone = request.POST["Phone"]
        company = request.POST["Company"]

        var = ContactDetails(Name=name, Email=email, Phone_number=phone, Company=company)
        var.save()
    return render(request, 'frontpage1/contact.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('Aman:home')
    else:
        form = UserForm
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + 'has been registered')
                return redirect('Aman:login')

        return render(request, 'frontpage1/register.html', {'form': form})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Aman:home')
        else:
            messages.info(request, 'Username or Password is wrong')

    return render(request, 'frontpage1/login.html')


def logoutpage(request):
    logout(request)
    return redirect('Aman:login')
